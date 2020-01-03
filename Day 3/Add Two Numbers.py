class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    carry = 0 # carry equals zero
    root = n = ListNode(0) #  root and n equals a new listnode.
    while l1 or l2 or carry:

      v1 = v2 = 0 # v1 and v2 equal zero
      if l1: # while going through l1
        v1 = l1.val # v1 will be equal to the value in the current node
        l1 = l1.next # go to the next value in the List.

      if l2:
        v2 = l2.val
        l2 = l2.next
      carry, val = divmod(v1 + v2 + carry, 10)  # divide the sum of v1,v2,  plus carry(carry0) and divide by 10. It will do this each time it goes through it.  unpacked
      n.next = ListNode(val) # adds val to the listnode
      n = n.next
    return root.next