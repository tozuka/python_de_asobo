# -*- coding: utf-8 -*-
import math
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *

##
## §1.1 簡単な近似
##
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

#import functools
#phi01 = functools.partial(step_func, 0.0, 1.0)
#for i in range(-5, 6):
#    r = 0.5 * i
#    print "phi(%g) = %g" % (r, phi01(r))

#def samplepoints(start,end,n):
#  w = end - start
#  return map(lambda i:start+w*i/n, range(n+1))

#m = 12
#f = lambda x:math.sin(x*2)+math.cos(x*3)
#sj = map(f, rj)

# print sj
#def sigma(n, f):
#  sum(map(f,n))


def makefn(f, m):
  lower = 0.0
  upper = 1.0
  unit = (upper - lower) / m;
  rj = arange(lower, upper, unit)
  sj = map(f, rj)
  def fn(x):
    return sum(map(lambda r,s:s*step_func(r,r+unit,x),
                   rj,sj))
  return fn

#    sum(map(rj,
#print "t: ", t

fn = lambda x:sin(3.1*pi*x)+cos(2.4*pi*x)
f1 = makefn(fn,8)

t = arange(0.0, 1.0, 0.001)
s = map(f1,t)
plot(t, s, linewidth=0.5)
#xlabel('time (s)')
#ylabel('voltage (mV)')
#title('hello')
grid(True)
show()


def _test():
  import doctest
  doctest.testmod()

if __name__ == "__main__":
  _test()

