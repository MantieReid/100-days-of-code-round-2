import collections
from collections import Counter
from typing import List
from self import self
class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    counthem = collections.Counter(nums) # counter to get the number of times each element appears in the list.
    duplicates = [x for x in counthem if counthem[x]> 1] # if the element occurs more one time, add it to the list called duplicates
    print(duplicates) # print out the list called duplicates
    return duplicates # return the list called duplicates


somenums = [4,3,2,7,8,2,3,1]

Solution.findDuplicates(self,nums=somenums)
