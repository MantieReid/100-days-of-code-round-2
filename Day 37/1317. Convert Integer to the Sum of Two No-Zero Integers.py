from typing import List
from self import  self

class Solution:
  def getNoZeroIntegers(self, n: int) -> List[int]:
    for a in range(n):
      if '0' not in f'{a}{n - a}': # If zero is not in a(which is the range counter) and n-a(which is combined with a)
        return [a, n - a] # Then  Return a and n  minus a.



somenumber = 11

Solution.getNoZeroIntegers(self,n=somenumber)
