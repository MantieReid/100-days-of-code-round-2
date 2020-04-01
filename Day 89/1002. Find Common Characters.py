import collections
from typing import List

class Solution:
  def commonChars(self, A: List[str]) -> List[str]:
    res = collections.Counter(A[0]) # result is equal to a counter for the "A" list.
    for a in A:
      res &= collections.Counter(a)  # result will be equul to a counter and it will put it in a bitwise format as well.
    return list(res.elements())


