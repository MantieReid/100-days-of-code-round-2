import collections
from typing import List

from self import self

class Solution:
  def largestUniqueNumber(self, A: List[int]) -> int:
    return max([-1] + [k for k, v in collections.Counter(A).items() if v == 1])


somelist = [5,7,3,9,4,9,8,3,1]
Solution.largestUniqueNumber(self,A=somelist)

