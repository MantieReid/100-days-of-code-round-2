
#Invert a binary tree.
class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
      invert = self.invertTree # invert is equal to the tree.
      root.left, root.right = invert(root.right), invert(root.left) # root left is set to equal root right. Root right is set to equal the left.
    return root
