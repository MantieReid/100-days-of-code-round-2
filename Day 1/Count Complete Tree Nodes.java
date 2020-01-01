
/**
*Given a complete binary tree, count the number of nodes.


     * Definition for a binary tree node.
     * public class TreeNode {
     *     int val;
     *     TreeNode left;
     *     TreeNode right;
     *     TreeNode(int x) { val = x; }
     * }
     */
    class Solution {
      public int countNodes(TreeNode root) {
        if (root == null) {  //if root  is null, then return zero.
          return 0;
        }
        if (root.left == null && root.right == null) {
          return 1;  // if root left and root right are null, then return null.
        }

        return 1 + countNodes(root.left) + countNodes(root.right);  // starts counting the nodes recursively.  Using BFS. 
      }
    }