import collections

from self import  self
class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    hsh1 = collections.Counter(list(s)) # gets the count of each character in the string. Puts it in a list

    hsh2 = collections.Counter(list(t)) # gets the count of each character in the string. puts the results in a list.
    print("apples")
    return list(hsh2 - hsh1)[0] # take the count from both strings and subtract them in a list format. Returns the character that did not return zero from the subtraction.


s2 = "abcd"
t2 = "abcde"


Solution.findTheDifference(self,s = s2, t = t2)
