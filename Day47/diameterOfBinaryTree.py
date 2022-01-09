"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
                    1
                  2   3
                4  5

Output : 3
Explanation: [4->2->1->3] or [5->2->1->3]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        
        ## using depth-first search.
        ## define two parameters. Height and diameter. 
        res = [0]
        
        def dfs(root):
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            
            ## return a diameter.
            res[0] = max(res[0], 2 + left + right)
            
            ## return a height 
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]