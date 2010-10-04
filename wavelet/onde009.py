# -*- coding: utf-8 -*-
import math
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *

# 1.1 簡単な近似
def phi(lower,upper):
  def fn(r):
    if lower <= r < upper:
      return 1
    else:
      return 0
  return fn

def data2fn(data):
  m = len(data)
  lower = data[0][0]
  unit  = data[1][0] - data[0][0]
  upper = data[m-1][0] + unit
  rj = map(lambda x:x[0], data)
  sj = map(lambda x:x[1], data)
  pj = map(lambda ri:phi(ri,ri+unit), rj)
  def fn(r):
    return sum(map(lambda pi,si:si*pi(r), pj,sj))
  return fn

def makefn(f, m):
  lower = 0.0
  upper = 1.0
  unit = (upper - lower) / m;
  rj = arange(lower, upper, unit)
  sj = map(f, rj)
  return data2fn(zip(rj,sj))


def graph(lower,upper,*fs):
  t = arange(lower, upper, 0.001)
  for f in fs:
    plot(t, map(f,t), linewidth=0.5)
  # xlabel('time (s)')
  # ylabel('voltage (mV)')
  # title('hello')
  grid(True)
  show()

##
def psi(lower,upper):
  mid = (lower + upper)/2.
#  p1 = phi(lower, mid)
#  p2 = phi(mid, upper)
#  return lambda r:p1(r)-p2(r)
  def fn(r):
    if lower <= r < mid:
      return 1
    elif mid <= r < upper:
      return -1
  return fn


fn = lambda x:sin(3.1*pi*x)+cos(2.4*pi*x)
#graph(0., 1.,
#      fn,
#      makefn(fn,2),
#      makefn(fn,4),
#      makefn(fn,8),
#      makefn(fn,16)
#      )

def rjs(m): # [0, 1/m, 2/m, 3/m, ..., (m-1)/m ]
  return map(lambda x:1.0/m*x,range(m))

d11 = zip(rjs(2), [9,1])
d12 = zip(rjs(4), [5,1,2,8])
d13 = zip(rjs(8), [3,1,0,4,8,6,9,9])
d14 = zip(rjs(8), [8,6,7,3,1,1,2,4])
d15 = zip(rjs(8), [3,1,9,7,7,9,5,7])

d16 = d11
d17 = d12
d18 = d13
d19 = zip(rjs(2), [2,8])

def hwt(data):
  """Haar Wavelet Transformcd 
  [s0,s1,s2,s3,...,sn-1]
  -> ( [s'0,s'1,...], [s''0,s''1,...] )
  """
  sz = len(data)
  i = 0
  res1 = []
  res2 = []
  while i < sz:
    s0 = data[i]
    s1 = data[i+1]
    res1.append((s0+s1)/2.)
    res2.append((s0-s1)/2.)
    i += 2
  return (res1,res2)

def hwt2(data):
  """Haar Wavelet Transform
  [(r0,s0),(r1,s1),...(rn-1,sn-1)]
  --> ( [(r'0,s'0),...], [(r''0,s''0),...] )
  """
  sz = len(data)
  i = 0
  res1 = []
  res2 = []
  while i < sz:
    r0 = data[i][0]
    s0 = data[i][1]
    r1 = data[i+1][0]
    s1 = data[i+1][1]
    res1.append((r0, (s0+s1)/2.))
    res2.append((r0, (s0-s1)/2.))
    i += 2
  return (res1,res2)

#graph(0., 1., data2fn(d14) )
#print d17, " >> ", hwt(d17)
#print d18, " >> ", ab(d18)
#print hwt([5,1,2,8])




def _test():
  import doctest
  doctest.testmod()

if __name__ == "__main__":
  _test()

