from typing import List


class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    alist = []  # create a empty list
    for i in range(1, n + 1): #use range to generate the numbers to add to the list
      if i % 3 == 0 and i % 5 == 0: # if the number is a a multiple of 3 and five. Then add the string FizzBuzz to the list instead of that number.
        alist.append("FizzBuzz")
      elif i % 3 == 0:  # if the number is a multiple of 3, then add the word fizz to the list.
        alist.append("Fizz")
      elif i % 5 == 0: # if the number is  multiple of 5, then add the word buzz to the list.
        alist.append("Buzz")
      else: # else, add the current number to the list.
        alist.append(i)
    alist = list(map(str, alist))   # convert the elements of the list to a string.
    return alist  # return the list.
