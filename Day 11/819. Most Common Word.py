import collections
from typing import List
import re


paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned2 = ["hit"]

def mostCommonWord( paragraph: str, banned: List[str]) -> str:
  ban = set(banned) # turns the ban list into a set
  words = re.findall(r'\w+', paragraph.lower()) # turns the paragraph into a list. Removes everything elese except the strings.
  apples = collections.Counter(w for w in words if w not in ban).most_common(200)[0][0] # Determines which string occurs the most.  Returns it back in a list. Uses collections to help count it.
  return apples # returns the result



mostCommonWord(paragraph2,banned2)
