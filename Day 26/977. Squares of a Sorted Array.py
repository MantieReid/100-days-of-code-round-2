from typing import List


def sortedSquares( A: List[int]) -> List[int]:
  sorted_squared_list = []

  for x in A: #  Iterate through the list
    a = x**2 # times each element to the power of two
    sorted_squared_list.append(a) # append that result to the list

  x = sorted(sorted_squared_list) # sort the list

  #print(sorted_squared_list)  # prints out the list
  return x # return the list



#somelist = [-4,-1,0,3,10]
#somelist2 = [-7,-3,2,3,11]
#sortedSquares(somelist)
#sortedSquares(somelist2)
