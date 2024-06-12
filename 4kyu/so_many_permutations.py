# Create all permutations of a non-empty input string and remove duplicates, if present

from itertools import permutations as perms

def permutations(s):
  outarr = []
  perm = perms(list(s))
 
  for i in perm:
    j = ''.join(i)
    outarr.append(j) if j not in outarr else None

  return(outarr)
  