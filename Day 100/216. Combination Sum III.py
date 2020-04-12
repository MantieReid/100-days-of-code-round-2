from itertools import combinations
from typing import List
from self import  self

class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    a =  [c for c in combinations(range(1, 10), k) if sum(c) == n]
    return a



Solution.combinationSum3(self,k=3, n = 7)
