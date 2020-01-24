
class Solution:
  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

    def GetSum(root):
      rangesum = 0

      if root:
        if root.val > L:
          rangesum += GetSum(root.left)

        if  root.val < R:
          rangesum+= GetSum(root.right)

        if  root.val <=R and root.val >= L:
          rangesum+= root.val

      return rangesum


    return GetSum(root)

