import sys
import urllib
import unittest
import json


def HasResponse(response):
    data = json.load(response)
    return len(data)


class ElectionsTests(unittest.TestCase):
    HOST_NAME = 'http://50.116.6.242/'
    
    def test_HasElections(self):
        self.failUnless(HasResponse(urllib.urlopen(self.HOST_NAME+'api/elections/')))
        
    def test_HasPrecincts(self):
        self.failUnless(HasResponse(urllib.urlopen(self.HOST_NAME+'api/precincts/')))
        
def main():
    unittest.main()
    
if __name__ == '__main__':
  main()