from typing import List

from self import self

test23 = [1,3,4,2,2]
test50 = [3,1,3,4,2]

def findDuplicate(self, nums: List[int]) -> int:
  t = nums[0]  # T is equal to the first element in the index
  h = nums[nums[0]]
  while t != h:
    t = nums[t]
    h = nums[nums[h]]
  t = 0
  while t != h:
    t = nums[t]
    h = nums[h]
  print(t)
  return  t

findDuplicate(self,[1,3,4,2,2])
findDuplicate(self,nums=test50)

