from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
  current_index = 0
  while current_index < len(nums) - 1: # iterate through the list until the next to last element
    if nums[current_index] == nums[current_index+1]: # if both the current and the next element are the same
      del nums[current_index] # delete the current element
      current_index -=1 # to stay at the same place in the list, we decrease our index by one.
    current_index += 1 # then add one to keep going further in the list.

    return len(nums)
