from self import self

class Solution:
  def addDigits(self, num: int) -> int:
    while num >= 10: # while num is greater than or equal to ten.
      num = sum(list(map(int, str(num)))) # get the sum of the two numbers when spilt via a list. When the result becomes less than 10, return it.
      print(num)
    return num

Solution.addDigits(self, num=934334565465346546542342423654645643654756476576576534554767345456678567835476576853645466547654756454365765743542343242342567765)

