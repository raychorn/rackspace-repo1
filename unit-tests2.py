import unittest

def palindrome_test_function():
    def is_palindrome(S):
        pali = True
        SS = ''.join([s for s in str(S).lower() if (s.isalpha())])
        for i in xrange (0, len(SS) // 2):
            if SS[i] == SS[(i * -1) - 1] and pali is True:
                pali = True
            else:
                pali = False
                break
        return pali
    return is_palindrome

class MyUnitTests(unittest.TestCase):
    def test1(self):
        test_function = palindrome_test_function()
        self.assertTrue(test_function('Doc, note: I dissent. A fast never prevents a fatness. I diet on cod'))
        self.assertFalse(test_function('I am not one for sure'))
        self.assertTrue(test_function('Able was I ere I saw Elba'))
        self.assertTrue(test_function('Never odd or even'))
        self.assertTrue(test_function('aabbccddeefeeddccbbaa'))
        self.assertFalse(test_function('abbccddeeffeddccbbaa'))

if (__name__ == '__main__'):
    unittest.main()
    