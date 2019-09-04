import unittest
from pnv import isValid

class TestIsValid(unittest.TestCase):

  def testShouldValidateSampleNumber(self):
    result = isValid('678-839-6663')
    self.assertTrue(result)
    
    
  def testNoneShouldNotBeValid(self):
    result = isValid(None)
    self.assertFalse(result)
