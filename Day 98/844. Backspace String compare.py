class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    def build(S):
      ans = [] # create a stack
      for c in S: # loop through s
        if c != '#': # if c does not equal #
          ans.append(c) # append it to the list
        elif ans:
          ans.pop() # remove from the stack
      return "".join(ans) # return the ans as joined with the other string

    return build(S) == build(T) # return if string S is equal to string T. 
