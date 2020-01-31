class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    # if the len of the list is not equal to the length when it is a set. Then it contains duplicates. Return false
    # if it does not contain duplicates, then it should be equal in size when it is a set, then return true.
    return len(nums) != len(set(nums))
