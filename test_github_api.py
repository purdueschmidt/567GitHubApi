from unittest import main, TestCase
from unittest.mock import Mock, patch,MagicMock,PropertyMock
from  github_api import RepoData
import  github_api
from github import Github

import unittest

#from github import Github


class mock_repo:
    name = 'test'
    def get_repos(self,user):
        return []  
    def get_commits(self):
        return []
    
    def get_user(self,username):
        pass
    
class TestGithubApi(TestCase):

    @patch('github_api.Github')
    def test_no_repo(self, mock_Github):
        repodata = RepoData()
 

        mock_Github.get_user.return_value.get_repos.return_value = []


        ret = repodata.getRepoInfo(mock_Github, 'test')

        mock_Github.get_user.assert_called_once_with('test')
        mock_Github.get_user.return_value.get_repos.assert_called_once()
        mock_Github.get_commits.assert_not_called()

        assert ret == ''
    
    @patch('github_api.Github')
    def test_single_repo_one_commit(self, mock_Github):
        repodata = RepoData()
 
        inst = Mock(spec=mock_repo)
        mock_Github.get_user.return_value.get_repos.return_value = [inst]

        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.return_value = [2]
        
        p=PropertyMock(return_value='Mocked_Name')
        type(inst).name=p

        ret = repodata.getRepoInfo(mock_Github, 'test')
        
        mock_Github.get_user.assert_called_once_with('test')
        mock_Github.get_user.return_value.get_repos.assert_called_once()
        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.assert_called_once()
        assert ret == 'Repo: Mocked_Name Number of commits: 1\n'

    @patch('github_api.Github')
    def test_single_repo_no_commit(self, mock_Github):
        repodata = RepoData()
 
        inst = Mock(spec=mock_repo)
        mock_Github.get_user.return_value.get_repos.return_value = [inst]

        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.return_value = []

        p=PropertyMock(return_value='Mocked_Name')
        type(inst).name=p

        ret = repodata.getRepoInfo(mock_Github, 'test')
        
        mock_Github.get_user.assert_called_once_with('test')
        mock_Github.get_user.return_value.get_repos.assert_called_once()
        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.assert_called_once()
        assert ret == 'Repo: Mocked_Name Number of commits: 0\n'
        
    @patch('github_api.Github')
    def test_single_repo_multi_commit(self, mock_Github):
        repodata = RepoData()
 
        inst = Mock(spec=mock_repo)
        mock_Github.get_user.return_value.get_repos.return_value = [inst]

        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.return_value = [1,1,1,1,1]

        p=PropertyMock(return_value='Mocked_Name')
        type(inst).name=p

        ret = repodata.getRepoInfo(mock_Github, 'test')
        
        mock_Github.get_user.assert_called_once_with('test')
        mock_Github.get_user.return_value.get_repos.assert_called_once()
        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.assert_called_once()
        assert ret == 'Repo: Mocked_Name Number of commits: 5\n'
        
    @patch('github_api.Github')
    def test_multi_repo_commit_one_none(self, mock_Github):
        repodata = RepoData()
 
        inst = Mock(spec=mock_repo)
        inst2 = Mock(spec=mock_repo)
        mock_Github.get_user.return_value.get_repos.return_value = [inst,inst2]

        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.return_value = [1]
        mock_Github.get_user.return_value.get_repos.return_value[1].get_commits.return_value = []

        a=PropertyMock(return_value='Mocked_Name')
        type(inst).name=a
        b=PropertyMock(return_value='Mocked_Name2')
        type(inst2).name=b

        ret = repodata.getRepoInfo(mock_Github, 'test')

        mock_Github.get_user.assert_called_once_with('test')
        mock_Github.get_user.return_value.get_repos.assert_called_once()
        mock_Github.get_user.return_value.get_repos.return_value[0].get_commits.assert_called_once()
        mock_Github.get_user.return_value.get_repos.return_value[1].get_commits.assert_called_once()
        assert ret == 'Repo: Mocked_Name Number of commits: 1\nRepo: Mocked_Name2 Number of commits: 0\n'
        
if __name__ == '__main__':
    main()
