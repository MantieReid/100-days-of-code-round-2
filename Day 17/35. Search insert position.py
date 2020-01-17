
def searchInsert(self, nums: List[int], target: int) -> int:
  a = bisect.bisect_left(nums,target)
  return  a



