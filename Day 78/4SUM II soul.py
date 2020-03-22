import collections
import json
from typing import List


class Solution:
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    AB = collections.Counter(a+b for a in A for b in B) # tells us how many numbers of each we have when we add both A list and B list.
    print(sum(AB[-c-d] for c in C for d in D)) #
    return  sum(AB[-c-d] for c in C for d in D)

