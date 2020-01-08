# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummyroot = ListNode(0) # create a new linkedlist called dummyroot
    mergedlist = [] # create a new list called merged list. Which will store the values of both L1 and L2
    while l1 or l2: # Iterate through the list, even if one of the list is empty
      if l1 == None: # if empty, then skip it and do the next list l2
        mergedlist.append(l2.val)
        l2 = l2.next
      elif l2 == None: # if l2 is empty, then do the l1 linked list.
        mergedlist.append(l1.val)
        l1 = l1.next
      else: # else, add values from them and add it to the merge sort list
        mergedlist.append(l1.val)  # add l1.val to the list
        l1 = l1.next
        mergedlist.append(l2.val)  # add l2 val to the list
        l2 = l2.next

    mergedlist.sort() # sort the list.
    dummy_linked_list = dummyroot # Dummy linked list is equal to dummy root
    for x in mergedlist:  # iterate through the elements of merged list.
      dummy_linked_list.next = ListNode(x) # set the next val to be the current item from merge list. Using Listnode for type conversion
      dummy_linked_list = dummy_linked_list.next
    dummy_linked_list = dummyroot.next
    return dummy_linked_list
