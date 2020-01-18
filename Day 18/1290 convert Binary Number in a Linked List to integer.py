
class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    somelist = [] # a empty list to hold the values from the head linked list
    while head: # iterate through the list
      somelist.append(head.val) # add the value to the list
      head = head.next # go to next node

    values = ''.join(str(v) for v in somelist) # merge all the elements in the list into one str
    BinaryToDecimal = int(values,2) # convert it to a decimal
    return BinaryToDecimal # return the result of the conversion


