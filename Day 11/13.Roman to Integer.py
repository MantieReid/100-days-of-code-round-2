class Solution:
  def romanToInt(self, s: str) -> int:
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
             'I': 1}  # a dictionary to define each big roman value up to 1000
    # Roman will be used to convert it to a number.
    z = 0  # set up z
    for i in range(0, len(s) - 1):  # iterate starting at index zero, and end at the length of the string   minus one.
      if roman[s[i]] < roman[s[
        i + 1]]:  # Gets the value of the roman numeral  in a integer, only one character, and determines if it is  greater than the next element in the string.

        z -= roman[s[i]]  # subtract the roman numeral  converted integer from z.
      else:
        z += roman[s[i]]  # add the element to z.
    return z + roman[s[-1]]  # Z plus  the last character/ roman integer in the string

