# -*- coding: utf-8 -*-

##
## 1.4
##

def log2(x):
  n = 0
  while x > 1:
    x /= 2
    n += 1
  return n

# print log2(1), log2(2), log2(4), log2(8), log2(15), log2(16)

def IpFHWT(s,sw=-1):
  """置換高速ハールウェーブレット変換"""
  m = len(s)
  n = log2(m)
  if sw < 0: sw = n
  i = 1
  j = 2
  loop = 0
  while loop < sw:
    m /= 2
    k = 0
    while k < m:
      s0 = s[j*k]
      s1 = s[j*k+i]
      s[j*k]   = (s0 + s1)/2.
      s[j*k+i] = (s0 - s1)/2.
      k += 1
    i = j
    j *= 2
    loop += 1
  return s

def assert_equal(a,b):
  if a == b:
    print "OK:", a, "=", b
  else:
    print "FAIL:", a, "!=", b

# 例題1.17; [5,1,2,8] # = ...
assert_equal( IpFHWT([5,1,2,8],0), [5,1,2,8] )
assert_equal( IpFHWT([5,1,2,8],1), [3,2,5,-3] )
assert_equal( IpFHWT([5,1,2,8],2), [4,2,-1,-3] )
assert_equal( IpFHWT([5,1,2,8]), [4,2,-1,-3] )

# 例題1.18; [3,1,0,4,8,6,9,9] # = ex1.4
assert_equal( IpFHWT([3,1,0,4,8,6,9,9],0), [3,1,0,4,8,6,9,9] )
assert_equal( IpFHWT([3,1,0,4,8,6,9,9],1), [2,1,2,-2,7,1,9,0] )
assert_equal( IpFHWT([3,1,0,4,8,6,9,9],2), [2,1,0,-2,8,1,-1,0] )
assert_equal( IpFHWT([3,1,0,4,8,6,9,9],3), [5,1,0,-2,-3,1,-1,0] )
assert_equal( IpFHWT([3,1,0,4,8,6,9,9]), [5,1,0,-2,-3,1,-1,0] )


##
## 1.5
##

def IpIHWT(s,sw=-1):
  m = len(s)
  n = log2(m)
  if sw < 0: sw = n
  i = 2**(n-1)
  j = 2*i
  loop = 0
  m = 1
  while loop < sw:
    k = 0
    while k < m:
      s0 = s[j*k]
      s1 = s[j*k+i]
      s[j*k] = s0 + s1
      s[j*k+i] = s0 - s1
      k += 1
    j = i
    i /= 2
    m *= 2
    loop += 1
  return s

# 例題1.20
assert_equal( IpIHWT([5,4],0), [5,4] )
assert_equal( IpIHWT([5,4],1), [9,1] )
assert_equal( IpIHWT([5,4]), [9,1] )

# 例題1.21
assert_equal( IpIHWT([4,2,-1,-3],0), [4,2,-1,-3] )
assert_equal( IpIHWT([4,2,-1,-3],1), [3,2,5,-3] )
assert_equal( IpIHWT([4,2,-1,-3],2), [5,1,2,8] )
assert_equal( IpIHWT([4,2,-1,-3]), [5,1,2,8] )

##
## 1.6
##
suion = [
    32.0, 10.0, 20.0, 38.0, 37.0, 28.0, 38.0, 34.0,
    18.0, 24.0, 18.0,  9.0, 23.0, 24.0, 28.0, 34.0 ]

output_expected = [
    25.9375, 11.0, -4.0,  -9.0,
    -4.625,   4.5, -1.75,  2.0,
     3.6875, -3.0,  3.75,  4.5,
    -5.0,    -0.5, -3.75, -3.0 ]

assert_equal( IpFHWT(suion), output_expected )

output_must_be = [
        25.9375,
        3.6875,
        -4.625, -5.0,
        -4.0, -1.75, 3.75, -3.75,
        11.0, -9.0, 4.5, 2.0, -3.0, 4.5, -0.5, -3.0 ]



