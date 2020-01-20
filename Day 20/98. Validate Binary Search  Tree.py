# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    stack = [] # to hold the binary tree itself
    prev = None # to compare with the

    while root or stack:
      while root:
        stack.append(root) # adds the binary tree to the list
        root = root.left # root is set to be equal to its left node
      root = stack.pop() # pops the last item in the list.

      if prev and root.val <= prev.val: # if the prev and root.val are less than the previous value/node then return false
        return False # not a balanced tree
      prev = root # or elese have prev equal to root
      root = root.right # root will be set to equal root right
      return True


def stringToTreeNode(input):
  input = input.strip()
  input = input[1:-1]
  if not input:
    return None

  inputValues = [s.strip() for s in input.split(',')]
  root = TreeNode(int(inputValues[0]))
  nodeQueue = [root]
  front = 0
  index = 1
  while index < len(inputValues):
    node = nodeQueue[front]
    front = front + 1

    item = inputValues[index]
    index = index + 1
    if item != "null":
      leftNumber = int(item)
      node.left = TreeNode(leftNumber)
      nodeQueue.append(node.left)

    if index >= len(inputValues):
      break

    item = inputValues[index]
    index = index + 1
    if item != "null":
      rightNumber = int(item)
      node.right = TreeNode(rightNumber)
      nodeQueue.append(node.right)
  return root


def main():
  import sys
  import io
  def readlines():
    for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
      yield line.strip('\n')

  lines = readlines()
  while True:
    try:
      line = next(lines)
      root = stringToTreeNode(line);

      ret = Solution().isValidBST(root)

      out = (ret);
      print(out)
    except StopIteration:
      break


if __name__ == '__main__':
  main()
