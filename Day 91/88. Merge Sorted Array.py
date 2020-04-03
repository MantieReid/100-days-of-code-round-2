from typing import List


class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[:] = sorted(nums1[:m] + nums2)  # merge both lists and sort them.
    """
    Do not return anything, modify nums1 in-place instead.
    """
