from typing import List

from self import  self

class Solution:
  def heightChecker(self, heights: List[int]) -> int:
    s = sorted(heights) # sorts the list
    ans = 0 # ans is equal to zero
    for h, hs in zip(heights, s):
      if h != hs: # if h is not equal to hs
        ans += 1 # increment ans by one
    return ans # return ans




heights23 = [1,1,4,2,1,3]

Solution.heightChecker(self,heights23)
