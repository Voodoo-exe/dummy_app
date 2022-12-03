import unittest
from app import calc
import sys
sys.path.append('../')


class UnitTestCalc(unittest.TestCase):
    def testUndefined(self):
        self.assertEquals(calc(5, 0, 'Division'), 'Undefined')


if __name__ == '__main__':
    unittest.main()
