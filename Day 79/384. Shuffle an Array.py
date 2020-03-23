from typing import List
import random
class Solution(object):
  def __init__(self, nums: List[int]):
    self.nums = nums # have nums equal to itself
    self.original = nums[:] # orginal is equal to the nums list.

  def reset(self) -> List[int]:
    self.nums = self.original[:] # have nums be equal to its original self
    return  self.nums # return the list
    """
    Resets the array to its original configuration and return it.
    """

  def shuffle(self) -> List[int]:
    random.shuffle(self.nums) # return the list in a different order.
    return self.nums
    """
    Returns a random shuffling of the array.
    """

apples = [1,2,3]


