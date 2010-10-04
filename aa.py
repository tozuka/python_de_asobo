# -*- coding: utf-8 -*-

def sum(iota,fn):
  return reduce(lambda x,y:x+fn(y), iota, 0)

def prod(iota,fn):
  return reduce(lambda x,y:x*fn(y), iota, 1)


# y(x,<w>) = w_0 + w_1*x + w_2*x**2 + ... + w_m*x**M
#          = sigma (j=0..M) w_j * x**j
def y(x,w):
# x:scalar, w:vector[0..M]
#  M=len(w)-1
#  return sum(range(0,M+1), lambda j:w[j]*x**j);  # 14.4u, 11.3u
  xj,sum = 1.,0.
  while w:
    xj,sum = xj*x, sum+w.pop(0)*xj
  return sum

#def E(x,t,w):
# x: vector [1..N]
# t: vector [1..N]
# w: vector [0..M]


import unittest

class TestIroiro(unittest.TestCase):
#  def __init__(self):
#    print("いろいろテスト")

  def setUp(self):
    pass

  def testRange(self):
    print("\nrange() の確認")
    self.assertEqual([0,1,2,3], range(4))
    self.assertEqual([0,1,2,3], range(0,4))
    self.assertEqual([1,2,3], range(1,4))
    self.assertEqual([2,3], range(2,4))

  def testSum(self):
    print("\nsum - Σ関数")
    self.assertEqual(45, sum(range(1,10), lambda x:x))
    self.assertEqual(285, sum(range(1,10), lambda x:x*x))

  def testProd(self):
    print("\nprod - Π関数")
    self.assertEqual(362880, prod(range(1,10), lambda x:x))
    self.assertEqual(131681894400L, prod(range(1,10), lambda x:x*x))

  def testY(self):
    print("\ny - y(x,w)")
    ## expects 1 + 2*2 + 3*4 + 4*8 = (+ 1 4 12 32) = 49
    for i in range(10000):
      self.assertEqual(49, y(2, [1,2,3,4]))

if __name__ == '__main__':
  unittest.main()
