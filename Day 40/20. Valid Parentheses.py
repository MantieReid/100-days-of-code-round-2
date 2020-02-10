class Solution:
  def isValid(self, s: str) -> bool:
    stack = [0]
    mapping = {0: None, '(': ')', '[': ']', '{': '}'} # create a dictionary that holds both sides of the brackets. Zero to help check if the stack is empty
    for c in s: # iterate through string.
      if c in mapping: # check to see if the string contains anything from the dictionary called mapping.
        stack.append(c) # if a character from the string contains anything from the dict, add it to the stack.
      else:
        if mapping[stack.pop()] != c: return False # if the character that is removed from the stack does not match c, then return false. The brackers are not matching up.
    return stack == [0] # return true or false if the stack(really the string) is empty or not.
