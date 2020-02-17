import collections

from self import  self
from typing import List


class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    C = collections.Counter
    apples = list((C(nums1) & C(nums2)).elements()) # returns the intersection of both lists. It returns the elements as it was counted the number of times in both lists.
    print(apples)
    return list((C(nums1) & C(nums2)).elements())



nums123 = [4,9,5]
nums24 = [9,4,9,8,4]

Solution.intersect(self,nums1=nums123,nums2=nums24)

