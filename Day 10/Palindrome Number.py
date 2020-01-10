class Solution:
  def isPalindrome(self, x: int) -> bool:
    Paldindrome_Check =  str(x) == str(x)[::-1] # checks to see if the int is the same number when it is outputted in reverse
    if Paldindrome_Check is True: # if the number turns out to be a palindrome
      return  True # then return true
    else: # if it is not a palindrome
      return  False # return false

