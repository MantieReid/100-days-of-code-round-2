from typing import List
def uncommonFromSentences( A: str, B: str) -> List[str]:
  result = [] # create a new list called result
  both = A.split(' ') + B.split(' ')  # Convert both string a and b into a list called both.

  for x in both: #  Iterate through the list
    if both.count(x)==1: # if the word only occurs once in the list

      result.append(x) # then add the word to list called result.
  return result
