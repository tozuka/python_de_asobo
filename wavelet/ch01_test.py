import random
import unittest

from ch01_03 import sweep

class TestChapter01(unittest.TestCase):
  def setUp(self):
#   self.seq = range(10)
    pass

  def testsweep(self):
    self.assertEqual(sweep([5,1,2,8]), [[4],[-1],[2,-3]])

#  def testchoice(self):
#    element = random.choice(self.seq)
#    self.assert_(element in self.seq)


if __name__ == '__main__':
    unittest.main()

