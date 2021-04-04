from github import Github

class RepoData:
    
    def __getRepos(self,gitApi,username):
        return gitApi.get_user(username).get_repos()

    def __getNumCommits(self,repo):
        commits = repo.get_commits()
        return len(list(commits))    

    def getRepoInfo(self,gitApi,username):
        repos = self.__getRepos(gitApi,username)
        text = ''
        for repo in repos :
            numCommits = self.__getNumCommits(repo)
            text += 'Repo: ' + repo.name + ' Number of commits: ' + str(numCommits) + '\n'
            
        return text


if __name__ == '__main__':
    repodata = RepoData()
    gitApi = Github()
    
    username = input('Enter a Github username.')
 
    print(repodata.getRepoInfo(gitApi, username))
