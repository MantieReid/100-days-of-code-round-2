class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      somelist = []  # create a new list
      dummyroot = ListNode(0) #  # create a new list

      while head: # iterate through the list
        somelist.append(head.val)  #add the current val from head to the list
        head = head.next # go to the next value in the list

      ptr = dummyroot # have ptr equal dummy root

      for x in reversed(somelist): # iterate through the somelist in reverse order
        ptr.next = ListNode(x) # add the value from the somelist to the new linked list
        ptr = ptr.next # go to to the next value in the list
      ptr = dummyroot.next # have ptr be equal to dummyrooot.next. This will allow it to return the entire list of Dummyroot when called.
      return ptr # return the Linked List
