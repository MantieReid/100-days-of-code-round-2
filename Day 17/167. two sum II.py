class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    index1 = 0
    index2 = len(numbers) - 1
    while index1 < index2:  # while index1 is less than index 2. Basically keep going until their equal or index one is greater than index 2
      if numbers[index1] + numbers[index2] == target:  # if the sum of both numbers is equal to the target
        return [index1 + 1, index2 + 1]  # then return their index postions plus one
      elif numbers[index1] + numbers[index2] > target:  # else if the sum of them are both greater than the target
        index2 -= 1  # decrease index 2 by one(go further into the list by moving down left)
      else:
        index1 += 1  # increase index one by one, tells it to go further into the list by moving right.
    return []  # return blank if none of the numbers add up to the sum
