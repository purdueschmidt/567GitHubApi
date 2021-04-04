from unittest import main, TestCase
from  github_api import RepoData
import  github_api
from github import Github

import unittest

class stubRepo :
    def __init__(self,name,commits):
        self.name = name
        self.commits =commits
        
    def get_commits(self):
        return self.commits
    
class stubApi:

    def __init__(self,repos):
        self.repos = repos
        
    def get_user(self,username):
        return self
    
    def get_repos(self):
        return self.repos


class TestGithubApi(TestCase):
    
    def test_rediculus(self):
        repodata = RepoData()
        gitApi = Github()

        ret = repodata.getRepoInfo(gitApi, 'purdueschmidt')
        text=''
        for repo in gitApi.get_user('purdueschmidt').get_repos() :
            numCommits = len(list(repo.get_commits()))
            text += 'Repo: ' + repo.name + ' Number of commits: ' + str(numCommits) + '\n'
            
        assert ret == text

    def test_one_repo_multi_commits(self):
        repodata = RepoData()
        
        gitRepo = [stubRepo('repoa',[1,1])]
        gitApi = stubApi(gitRepo)

        ret = repodata.getRepoInfo(gitApi, 'purdueschmidt')
        assert ret == 'Repo: repoa Number of commits: 2\n'

    def test_one_repo_one_commits(self):
        repodata = RepoData()
        
        gitRepo = [stubRepo('repoa',[1])]
        gitApi = stubApi(gitRepo)

        ret = repodata.getRepoInfo(gitApi, 'purdueschmidt')
        assert ret == 'Repo: repoa Number of commits: 1\n'

    def test_multi_repo_one_commit(self):
        repodata = RepoData()
        
        gitRepo = [stubRepo('repoa',[1]),stubRepo('repob',[1])]
        gitApi = stubApi(gitRepo)

        ret = repodata.getRepoInfo(gitApi, 'purdueschmidt')
        assert ret == 'Repo: repoa Number of commits: 1\nRepo: repob Number of commits: 1\n'

if __name__ == '__main__':
    main()
