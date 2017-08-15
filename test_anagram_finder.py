
import unittest
import anagram_finder as ana

class TestAnagramFinder(unittest.TestCase):
    '''
    Our basic test class
    '''

    def test_anagram_finder1(self):
        '''
        Test anagram_finder with a small list of words in testdictionary1
        '''
        res = ana.main('testdictionary1')
        self.assertEqual(res, ['later, alert, alter, ratel, taler'])
        return res

    def test_anagram_finder2(self):
        '''
        Test anagram_finder with a small list of words in testdictionary2      
        '''
        res = ana.main('testdictionary2')
        self.assertEqual(res, [])
        return res

if __name__ == '__main__':
    unittest.main()