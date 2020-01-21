import math
def isPowerOfThree( n: int) -> bool:
  if (n == 0): # If n is equal to zero, return false
    return False
  while (n % 2 == 0): # if the remainder is zero
    n /= 2
  #print(n == 1)
  return n == 1
  #return n > 0 == 2 ** 19 % n # checks wheter the number is postive and whether it divides 3^19.


isPowerOfThree(1048576)

