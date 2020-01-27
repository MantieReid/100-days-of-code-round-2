from typing import List


def preorder(self, root: 'Node') -> List[int]:
  def PreorderTraversal(root2):
    res = []
    if root2:
      res.append(root2.data)
      res = res + self.PreorderTraversal(root2.left)
      res = res + self.PreorderTraversal(root2.right)
    return res

