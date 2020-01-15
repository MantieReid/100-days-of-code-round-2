
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    dummy_head = ListNode(-1) # dummyhead is defined as a new list node
    dummy_head.next = head # dummyhead.next is set to equal head

    current_node = dummy_head # current node is set to equal dummy_head.
    while current_node.next != None: # while the  next node is not empty.
      if current_node.next.val == val: # if the current next val is equal to val
        current_node.next = current_node.next.next # remove the val and set the previous pointer to be set to the next one.
      else:
        current_node = current_node.next # go on to the next node.

    return dummy_head.next





