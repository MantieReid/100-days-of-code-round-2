import collections
from self import self

from typing import List


class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    c = collections.Counter(arr)
    return len(c) == len(set(c.values()))


arr2  = [-3,0,1,-3,1,1,1,-3,10,0]

Solution.uniqueOccurrences(self,arr = arr2)
