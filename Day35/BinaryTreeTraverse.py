"""
Given the root of a binary tree, return the Preorder, Inorder and Postorder traversal of its nodes' values.

Ex: root = [1, null, 2, 3]
Return: LDR-> [1,3,2]
        VLR-> [1,2,3]
        LRD-> [3,2,1]

Using recursive solution

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        
        output = []
        
        def LDR(node): ## Inorder Traversal: left -> center -> right
            if not node:
                return 0
        
            LDR(node.left)
            output.append(node.val)
            LDR(node.right)
        
        LDR(root)
        return output

        def VLR(node): ## Preorder Traversal: center -> left -> right
            if not node:
                return 0
            
            output.append(node.val)
            VLR(node.left)
            VLR(node.right)
        
        VLR(root)
        return output
        
        def LRD(node): ## Postorder Traversal: left -> right -> center
            if not node:
                return 0
            
            LRD(node.left)
            LRD(node.right)
            output.append(node.val)
        
        LRD(root)
        return output