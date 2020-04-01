from typing import List
import collections
from self import self

class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    #countthis = collections.Counter(nums)
    aj =  set([i for i in nums if nums.count(i) == 1])
    somelist = []
    somelist.extend(aj)
    print(aj)
    print(somelist)
    return somelist


somelist22 = [1,2,1,3,2,5]
Solution.singleNumber(self,nums=somelist22)



