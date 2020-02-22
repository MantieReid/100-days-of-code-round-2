class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

