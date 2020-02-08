class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    zero = 0 # record the position of '0'

    index_number = 0
    end = len(nums) # end is equal to the length of the list
    while index_number < end: # while the index number is less than the size of the list
      if nums [index_number] == 0: # if the current indexed number is equal to zero
        del nums[index_number] # delete  that number from the list
        nums.append(0)  # add the zero number to the back of the list
        end -=1 # we tell this number to decrease in size by one. Because we dont want to end up counting the zeros we just added to the end of the list.  Or else it will end up in a infinity loop.
      else:
        index_number +=1 # to tell it to check the next number in the list.



    """
    Do not return anything, modify nums in-place instead.
    """
