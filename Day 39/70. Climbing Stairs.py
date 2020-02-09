class Solution:
  def climbStairs(self, n: int) -> int:
    a = b = 1
    for x in range(n):
      # a, b = b,  a + b
      z = a
      a = b
      b = z + b
    return a

