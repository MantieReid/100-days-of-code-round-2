class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    # basically using two pointers to go through the list.
    # slow will move by one step to the next node.
    # Fast will move by two steps to the next node
    slow = fast = head
    while fast and fast.next:
      slow = slow.next # slow will go to the next node
      fast = fast.next.next # fast will skip the next node and go to the one after it. 
    return slow
