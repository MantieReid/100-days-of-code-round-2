class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    return bin(x ^ y).count('1')  # returns the binary equivalent of x to the power of y. Then it counts the number of times "one" is found in the binary.

