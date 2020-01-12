# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

    if not t1 and not t2: return None # will return none if both trees are empty

    #ans is a new treenode
    # it is initialized with the sum of the first t1 value and the t2 value. However, if t1 tree is empty, then return zero for its value. If t2 is empty, then return zero for its value.
    ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))

    #for the left child of the tree, it will be the result of t1 left and t2 left merging. Done so recursively
    ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)

    #for the rigt side, it will merge with the right child of t1 and the right child of t2.  Done so recursively
    ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

    return ans #return the tree.

