import binascii

from self import self


class Solution:
  def addBinary(self, a: str, b: str) -> str:
    return '{0:b}'.format(int(a, 2) + int(b, 2))



Solution.addBinary(self,a = "11",b="1")
