class Solution:

  ''''' First, we start with the last number in the numbers list. Then we go ahead and determine which index it should be stored at in the sorted list.
   We use Bisect left to help keep the numbers sorted from small to big in the sorted list.
   That index number is then stored in the result list.
   Then we store the element from the numbers list at that same index position in the sorted list.
   Then, after we are done with iterating through the nums list, we return the results list.
   The results list tells us how many numbers are smaller than each other.
'''
  def countSmaller(self, nums: List[int]) -> List[int]:
    sortedList = []
    result = []
    for num in nums[::-1]: # Iterates through the list. Starting at the last index.
      postion = bisect_left(sortedList, num)  # checks to see where the number from nums list can be inserted.  Returns the index of where it can be placed to maintain sorted list.
      result.append(postion) # adds the index  number of where the element from nums can be placed in the sorted list.
      sortedList.insert(postion, num)  #adds the current selected element from nums list to the selected index postion in the sorted list.

    return result[::-1]
