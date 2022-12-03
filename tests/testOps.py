import sys
sys.path.append('../')
from app import calc
import unittest

class UnitTestCalc(unittest.TestCase):
    
    def testOperation(self):
        
        self.assertEquals(calc(4,5,'Addition'),9)
        self.assertEquals(calc(4,5,'Subtraction'),-1)
        self.assertEquals(calc(4,5,'Multiplication'),20)
        self.assertEquals(calc(4,5,'Division'), 0.8)
        
        

if __name__ == '__main__':
    unittest.main()