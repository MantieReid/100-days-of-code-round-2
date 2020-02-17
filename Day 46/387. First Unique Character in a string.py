class Solution:
  def firstUniqChar(self, s: str) -> int:
    letters = 'abcdefghijklmnopqrstuvwxyz'  # all the letters in the alphabet
    index = [s.index(l) for l in letters if s.count(l) == 1]  # equals the first unique character in the string
    return min(index) if len(index) > 0 else -1  # return the min of the index if string len is greater than zero.
