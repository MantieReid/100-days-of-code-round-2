from typing import List


def search( nums: List[int], target: int) -> int:
  try:
    a = nums.index(target)
    #print(a)
    return  a
  except:
    #print(-1)
    return  -1





nums23 = [-1, 0, 3, 5, 0, 12]

search(nums=nums23,target = 12)


