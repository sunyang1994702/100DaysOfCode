"""
Given the root of a binary tree, invert the tree, and return its root.


Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree_recursive(self, root):
        # Recursively. 
        if not root:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        temp = root.right
        root.right = self.invertTree_recursive(root.left)
        root.left = self.invertTree_recursive(temp)

        return root
    

    def invertTree_iterative(self, root):
        ## Iteratively
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            
            if node is not None:
                temp = node.right
                node.right = node.left
                node.left = temp
                
                stack.append(node.left)
                stack.append(node.right)
            
#             if node.left or node.right:
#                 temp = node.right
#                 node.right = node.left
#                 node.left = temp
                
#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
        return root
