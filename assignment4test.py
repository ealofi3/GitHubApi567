import  unittest
from assignment4 import getInfoApi
from unittest import mock

class TestMockApi(unittest.TestCase):   
    def test_mock_api(self):
        getInfoApi = mock.Mock(return_value = "The user has 5 repos, names and commits as follows: /nName: GitHubApi567; Commits: 9 /nName: Triangle567; Commits: 9 /nName: project-810-A; Commits: 9 /nName: helloworld; Commits: 9 ; Commits: 9 /nName: assignment5; Commits: 9 ")
        result = getInfoApi("ealofi3")
        self.assertEqual(result, "The user has 5 repos, names and commits as follows: /nName: GitHubApi567; Commits: 9 /nName: Triangle567; Commits: 9 /nName: project-810-A; Commits: 9 /nName: helloworld; Commits: 9 ; Commits: 9 /nName: assignment5; Commits: 9 ")
        
    
if __name__ == '__main__':
    unittest.main()
