# 202. Happy Number

"""Write an algorithm to determine if a number is "happy".

"A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers."
"""
def isHappy( n):
  stop = {1}
  while n not in stop:
    stop.add(n)
    n = sum(int(d) ** 2 for d in str(n))
  print("N is good")
  return n == 1


isHappy(1)
