import unittest
max_integer = __import__("6-max_integer").max_integer

class Testmaxint(unittest.Testcase):
    ''' unittest class for max_integer'''

    def test_empty(self):
        ''' tests if the list is empty '''
        testlist = []
        self.assertEqual(max_integer(testlist), None)

    def test_one(self):
        ''' tests when the list has only one element '''
        testlist = [9]
        self.assertEqual(max_integer(testlist), 7)

    def test_string(self):
        ''' tests a list of strings '''
        testlist = ['hi', 'what', 'is', 'the', 'max']
        self.assertEqual(max_integer(testlist), 'hi')

if __name__ == '__main__':
    unittest.main()
