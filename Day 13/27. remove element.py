class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    ycount = nums.count(val)

    i = 0
    while i < ycount:
      nums.remove(val)
      i += 1
    return len(nums)


