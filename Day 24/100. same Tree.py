
class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p and q:
      # checks too see if both the first value of q and p are the same.
      # Checks too see if left side of p and q are equal to each other
      # checks too see if right side of p and right side of q are equal to each other
      # if all proves to be true, then it returns true or false if one condontion proves to be false
      return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    # one final check, check too see if p and q are both empty.
    return p is q




