import unittest
from phnutils import isValid
from phnutils import normalize

class TestNormalize(unittest.TestCase):

  def testShouldNormalizeNumberWithDotSeparator(self):
    result = normalize("678.839.6663")
    self.assertEqual("6788396663", result)
    
  def testShouldNormalizeNumberWithDashSeparator(self):
    result = normalize("678-839-6663")
    self.assertEqual("6788396663", result)
    
  def testShouldNormalizeNumberWithBackslashSeparator(self):
    result = normalize("678/839/6663")
    self.assertEqual("6788396663", result)
    
  def testShouldNormalizeNumberWithAreaCodeInParens(self):
    result = normalize("(678) 839-6663")
    self.assertEqual("6788396663", result)
    
  def testShouldNotNormalizeNone(self):
    self.assertFalse(normalize(None))

class TestIsValid(unittest.TestCase):

  def testShouldValidateSampleNumber(self):
    result = isValid('678-839-6663')
    self.assertTrue(result)
    
    
  def testNoneShouldNotBeValid(self):
    result = isValid(None)
    self.assertFalse(result)
