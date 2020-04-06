from typing import List
from self import  self

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
      return 0
    profit = 0
    for i in range(1, len(prices)): # loops starting from one and ends at the end of the list
      if prices[i] - prices[i - 1] > 0: # if price minus the previous price is greater than zero
        profit += prices[i] - prices[i - 1] #Then add it as a profit to the profit list. Profit equals price minus the previous price.
    return profit

somwlist =  [7,1,5,3,6,4]


Solution.maxProfit(self,somwlist)

