import unittest

import sys
sys.path.append('../')
from app import calc


class UnitTestCalc(unittest.TestCase):

    def testAddition(self):
        self.assertEquals(calc(4, 5, 'Addition'), 9)

    def testSubtraction(self):
        self.assertEquals(calc(4, 5, 'Subtraction'), -1)

    def testMultiplication(self):
        self.assertEquals(calc(4, 5, 'Multiplication'), 20)

    def testDivision(self):
        self.assertEquals(calc(4, 5, 'Division'), 0.8)


if __name__ == '__main__':
    unittest.main()
