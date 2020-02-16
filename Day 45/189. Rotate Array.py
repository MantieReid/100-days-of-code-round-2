from typing import List
from self import self

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:

    i = -1 # i will equal negative one

    KNeg = -k # kneg will equal the negative of k

    while i > KNeg+-1: # while i is greater than negative K
      nums.insert(0,nums[i]) # add the element from the back of the list to the front of the list.
      print(nums) # print it out
      i+= -1 # decrease i by negative one

    i = -1 # set i to be equal to neg one
    i2 = 0 # i2 will equal zero
    while i2 < k: # while i2 is less than k.
      del nums[i] # keep deleting the last element in the list until I2 is greater than k.
      i2 +=1

    print(nums)





    """
    Do not return anything, modify nums in-place instead.
    """

somelist = [1,2,3,4,5,6,7]

Solution.rotate(self,nums=somelist,k=3)
