import itertools
from typing import List


class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    results = []  # store the permutations in here, after being converted.
    temp = []   # to hold the lists temporarily from the output of converting the tuples to lists
    permuations = list(itertools.permutations(nums))
    i = 0
    while i < len(permuations):  # while i is less than the length of i
      temp = list(permuations[i])  # convert one tuple to a list  and store it in temp.
      results.append(temp)  # add the converted tuple to results
      i += 1  # increase i by one so we can continue to go through the list
    return results   # return the results

