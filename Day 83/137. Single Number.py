from typing import List
from self import self

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    for x in nums:
      a = nums.count(x)
      if a == 1:
        print(x)
        return  x




somelist = [2,2,3,2]
Solution.singleNumber(self,nums=somelist)
