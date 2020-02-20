import unittest
import requests
from assignment4 import getInfoApi
class TestApi(unittest.TestCase):
    def test_Api(self):
        self.assertEqual(getInfoApi('ealofi3'), 'Right')
       
if __name__ == '__main__':
    unittest.main(verbosity=2)