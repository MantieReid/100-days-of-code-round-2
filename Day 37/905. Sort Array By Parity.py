from typing import List

from self import self

class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    newlist = [] # a new list

    for item in A: # iterate through the list
      mod = item % 2 # gets the remainder when divided by 2
      if mod == 0:  # if number is even
        newlist.append(item) # then add it to the list

    for item in A:

      mod = item % 2 # gets the remainder when divided by two

      if mod > 0: # if the remainder is greater than zero, then it is odd
         newlist.append(item) # add it to the list
    print(newlist)
    return newlist

somelist = [3,1,2,4]

Solution.sortArrayByParity(self,A=somelist)


