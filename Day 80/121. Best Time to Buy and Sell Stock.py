import json
from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    ## Soultion
    max_profit, min_price = 0, float('inf') # max profit is zero. min_price is set to a float.
    for price in prices: # loop through the price list.
      min_price = min(min_price, price) # min price is equal to the minimum of min price and min.
      profit = price - min_price # profit equals profit minus min price.
      max_profit = max(max_profit, profit) # get the maxium of maxium profit and profit as well.
    return max_profit
## End of soultion

def stringToIntegerList(input):
  return json.loads(input)


def main():
  import sys
  import io
  def readlines():
    for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
      yield line.strip('\n')

  lines = readlines()
  while True:
    try:
      line = next(lines)
      prices = stringToIntegerList(line);

      ret = Solution().maxProfit(prices)

      out = str(ret);
      print(out)
    except StopIteration:
      break


if __name__ == '__main__':
  main()
