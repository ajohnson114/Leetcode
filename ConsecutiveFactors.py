"""
This is a codility problem where you are given a number N and are asked to return the smallest of consecutive factors that multiply to N
if they exist otherwise return 0. The trick is that if such 2 factors exist, one must be smaller than sqrt(N) and one must be greater. 
Since they are consecutive factors, we can see if the floor and ceiling of the square root multiply to N and if they do we return the floor
and other wise return 0.
"""

import math
def ConsecutiveFactors(N):
  sqrt = math.sqrt(N)
  return math.floor(sqrt) if math.floor(sqrt)*math.ceil(sqrt) == N else 0
