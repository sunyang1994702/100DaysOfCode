"""
You are given two binary trees root1 and root2.
root1: [1,3,2,5].       root2: [2,1,3,null,4,null,7]
            1                           2
          3   2                       1   3
        5                              4   7
Output: [3,4,5,5,4,null,7]
                3
              4   5
            5 4   7

Just take a sumation of node's value for both trees. If the node was none then just return 0.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ## If both root1 and root2 are none, then return none
        if root1 is None and root2 is None:
            return None
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1 + v2) ## take a sumation of two nodes value.

        ## Run Depth-first search for left side of node.
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        ## Run Depth-first search for right side of node.
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return root
    