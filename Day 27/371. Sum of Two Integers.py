# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
class Solution:
  def getSum(self, a: int, b: int) -> int:
    somelist = [] # define a new list
    somelist.append(a) # add a to the list
    somelist.append(b) # add b to the list
    return sum(somelist) # return the sum of both adding A and B
