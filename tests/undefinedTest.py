import sys
sys.path.append('../')
from app import calc
import unittest

class UnitTestCalc(unittest.TestCase):
    
    def undefinedTest(self):
        
        self.assertEquals(calc(5,0,'Division'),'Undefined')

if __name__ == '__main__':
    unittest.main()