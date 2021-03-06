# -*- coding: utf-8 -*-
import math
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *
import functools

# 1.1 簡単な近似
def step_func(lower,upper,r):
  """ステップ関数

  >>> step_func(0.0, 1.0, -0.000001)
  0
  >>> step_func(0.0, 1.0, 0.0)
  1
  >>> step_func(0.0, 1.0, 0.000001)
  1
  >>> step_func(0.0, 1.0, 0.5)
  1
  >>> step_func(0.0, 1.0, 0.999999)
  1
  >>> step_func(0.0, 1.0, 1.0)
  0
  >>> step_func(0.0, 1.0, 1.000001)
  0
  """
  if lower <= r < upper:
    return 1
  else:
    return 0

def makefn(f, m):
  lower = 0.0
  upper = 1.0
  unit = (upper - lower) / m;
  rj = arange(lower, upper, unit)
  sj = map(f, rj)
  pj = map(lambda ri: functools.partial(step_func, ri, ri+unit),
           rj)
  def fn(r):
    return sum(map(lambda pi,si: si*pi(r),title('hello')

  grid(True)
  show()

def sample_to_fn(data): # 0..1
  lower = 0.0
  upper = 1.0
  unit = (upper - lower) / m;
  rj = arange(lower, upper, unit)
  sj = map(f, rj)
  pj = map(lambda ri: functools.partial(step_func, ri, ri+unit),
           rj)
  def fn(r):
    return sum(map(lambda pi,si: si*pi(r),title('hello')
  grid(True)
  show()


fn = lambda x:sin(3.1*pi*x)+cos(2.4*pi*x)
graph(0., 1.,
      fn,
      makefn(fn,2),
      makefn(fn,4),
      makefn(fn,8),
      makefn(fn,16)
      )

def rjs(m): # [0, 1/m, 2/m, 3/m, ..., (m-1)/m ]
  return map(lambda x:1.0/m*x,range(m))

  

d12 = zip(rjs(2), [9,1])
d13 = zip(rjs(4), [5,1,2,8])
d14 = zip(rjs(8), [3,1,0,4,8,6,9,9])

dq11 = zip(rjs(8), [8,6,7,3,1,1,2,4])
dq12 = zip(rjs(8), [3,1,9,7,7,9,5,7])


def _test():
  import doctest
  doctest.testmod()

if __name__ == "__main__":
  _test()

