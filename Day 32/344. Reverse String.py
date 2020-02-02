# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#You may assume all the characters consist of printable ascii characters.
from typing import List

from self import self


class Solution:
  def reverseString(self, s: List[str]) -> None:
    #print("apples")
    #print(s[:])  s[:] is equal to the list and s[::-1] is equal to the list in reverse
    s[:] = s[::-1]  # basically just take the list and have it equal to the reversal of the string.

    """
    Do not return anything, modify s in-place instead.
    """
somelist = ["h","e","l","l","o"]
Solution.reverseString(self,s=somelist)
