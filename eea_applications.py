import math


def extended_euclidean(a, b, verbose=False):
  """ Find a root (s, t) of the following equation:
    as + bt = gcd(a, b)

    Args:
      a (int): The first parameter.
      b (int): The second parameter.

    Returns:
      (int, int, int): A tupple of greatest common divisor, x, y respectively.
  """
  r = a;  r_ = b
  s = 1;  s_ = 0
  t = 0;  t_ = 1
  q = None
  while r_ != 0:
    if verbose:
      print '{:10s} {:10s} {:10s} {:10s}'.format(
          str(r), 
          str(q), 
          str(s), 
          str(t))
  
    q = r / r_
    r__ = r % r_
    r, s, t, r_, s_, t_ = (r_, s_, t_, r__, s - s_ * q, t - t_ * q)

  if verbose:
    print '{:10s} {:10s} {:10s} {:10s}'.format(
        str(r), 
        str(q), 
        str(s), 
        str(t))
    if s != 0:
      print '{:10s} {:10s} {:10s} {:10s}'.format(
          str(r / q),
          None, 
          str(-s / abs(s) * b / r), 
          str(s / abs(s) * a / r))
    else:
      print '{:10s} {:10s} {:10s} {:10s}'.format(
          str(r / q), 
          None, 
          str(-t / abs(t) * b / r), 
          str(t / abs(t) * a / r))
  
  return r, s, t


def fermat_euler(p, verbose=False):
  """ Find a root (a, b) of the following equation:
    a ** 2 + b ** 2 = p
    where p is a prime number satisfying p = 4 * k + 1

    Args:
      p (int): The prime number.

    Returns:
      (int, int): A tupple of a, b respectively.
  """

  def _get_sqrt_of_minus_1(p):
    for gamma in xrange(p):
      beta = pow(gamma, (p - 1) / 4, p)
      if (beta * beta + 1) % p == 0:
        return beta

  a = p; b = _get_sqrt_of_minus_1(p)
  r = a;  r_ = b
  s = 1;  s_ = 0
  t = 0;  t_ = 1
  q = None
  
  if verbose:
    print 'a = {}, b = {}'.format(a, b) 

  while r_ != 0:
    if verbose:
      print '{:10s} {:10s} {:10s} {:10s}'.format(
          str(r), 
          str(q), 
          str(s), 
          str(t))
  
    q = r / r_
    r__ = r % r_
    r, s, t, r_, s_, t_ = (r_, s_, t_, r__, s - s_ * q, t - t_ * q)
    
    if r <= int(math.sqrt(p)) + 1:
      break

  if verbose:
    print '{:10s} {:10s} {:10s} {:10s}'.format(
        str(r), 
        str(q), 
        str(s), 
        str(t))
  
  return r, abs(t)


def rational_reconstruct(a, b, boundary=10**9, verbose=True):
  """ Find an approximate fraction whose numerator and denominator
  are smaller than boundary.

  Args:
    a (int), b (int): The original number is b / a.
    boundary (int): How large a numerator and denominator can be.

  Returns:
    (int, int): A tupple of numerator and denominator of the 
    approximate fraction.
  """

  r = a;  r_ = b
  s = 1;  s_ = 0
  t = 0;  t_ = 1
  q = None
  
  if verbose:
    print 'a = {}, b = {}'.format(a, b) 

  while True:
    if verbose:
      print '{:10s} {:10s} {:10s} {:10s}'.format(
          str(r), 
          str(q), 
          str(s), 
          str(t))
  
    q = r / r_
    r__ = r % r_
    r, s, t, r_, s_, t_ = (r_, s_, t_, r__, s - s_ * q, t - t_ * q)
    
    if max(abs(s_), abs(t_)) > boundary:
      break

  if verbose:
    print '{:10s} {:10s} {:10s} {:10s}'.format(
        str(r), 
        str(q), 
        str(s), 
        str(t))
  
  return abs(s), abs(t)

