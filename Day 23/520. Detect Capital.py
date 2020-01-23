# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# 1. All letters in this word are capitals, like "USA".
# 2. All letters in this word are not capitals, like "leetcode".
# 3. Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

class Solution:
  def detectCapitalUse(self, word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()  # check  ifs the word is upper case or lower case usage, and if the word is a title.

