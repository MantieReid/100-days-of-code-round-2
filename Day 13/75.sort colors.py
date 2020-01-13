from typing import List
import bisect

test500 = [2,0,2,1,1,0]

def sortColors( nums: List[int]) -> None:
  newlist = []
  newlist.extend(test500)
  test500.clear()
  for x in newlist:
    p = bisect.bisect_left(nums,x)
    nums.insert(p,x)



sortColors(nums=test500)


