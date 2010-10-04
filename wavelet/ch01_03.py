# -*- coding: utf-8 -*-
##
## §1.3 順序高速ハールウェーブレット変換(OFHWT)
##  - ordered Fast Haar Wavelet Transform
##
def hwt(data):
  """Haar Wavelet Transform
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

def unhwt(a,c):
  sz = len(a)
  orig = []
  i = 0
  while i < sz:
    orig.append(a[i] + c[i])
    orig.append(a[i] - c[i])
    i += 1
  return orig

## 定義1.10

## φ_k^{(n-l)}(r) := ...
def phi_(n,l,k):
  u = 2 ** (l - n)
  lower = u * k
  upper = u * (k+1)
  def fn(r):
    if lower <= r < upper:
      return 1
    else:
      return 0
  return fn

## ψ_k^{(n-l)}(r) := ...
def psi_(n,l,k):
  u = 2 ** (l - n)
  lower = u * k
  mid   = u * (0.5 + k)
  upper = u * (k + 1)
  def fn(r):
    if lower <= r < mid:
      return 1
    elif mid <= r < upper:
      return -1
  return fn


# 1.3.1

# 1.3.2

### すっとばして結論だけ合わせてある
def sweep(a):
  sz = len(a)
  res = []
  while sz>1:
      b = hwt(a)
      a = b[0]
      c = b[1]
      res.append(c)
      sz /= 2
  res.append(a)
  res.reverse()
  return res

def unsweep(ac):
  sz = len(ac)
  res = []
  a = ac[0]
  i = 1
  while i<sz:
      a = unhwt(a,ac[i])
      i += 1
  return a

#a2 = [5,1,2,8]
#print sweep(a2)

# sweep#1
def ppsweep(data):
  print data, " => ", sweep(data)

def ppunsweep(sweeped_data):
  print unsweep(sweeped_data), " <= ", sweeped_data

def ppsweep_vv(data):
  print data, " => ", sweep(data), " => ", unsweep(sweep(data))

def ppunsweep_vv(sweeped_data):
  print sweep(unsweep(sweeped_data)), " <= ", unsweep(sweeped_data), " <= ", sweeped_data


##
## §1.4 置換高速ハールウェーブレット変換(IpFHWT)
##  - In-Place Fast Haar Wavelet Transform
##
## 単に元の配列を上書きするだけ

def ipsweep(ar):
  pass

