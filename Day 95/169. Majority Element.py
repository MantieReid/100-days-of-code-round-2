from typing import List
import collections
from self import  self

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    majorityCount = len(nums)//2

    a = collections.Counter(nums)

    for x in a: # loop through the counter list
      if a[x] > majorityCount: # if x is greater than
        print(x)
        return x

whatever = [3,2,3]
whatever2 = [2,2,1,1,1,2,2]

Solution.majorityElement(self, nums=whatever2)

