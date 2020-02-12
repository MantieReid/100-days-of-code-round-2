# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val # set the value of the node want to delete to value of the node after it.
        node.next = node.next.next # then change the next pointer to point to the node after the next node.
