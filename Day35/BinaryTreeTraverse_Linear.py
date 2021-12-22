"""
Given the root of a binary tree, return the Preorder, Inorder and Postorder traversal of its nodes' values.

Ex: root = [1, null, 2, 3]
Return: LDR-> [1,3,2]
        VLR-> [1,2,3]
        LRD-> [3,2,1]

Using linear solution

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def LDR(self, root: TreeNode): ## Inorder Traversal: left -> center -> right
        
        output = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                ## using stack. Last in fiirt out
                holder = stack.pop()
                output.append(holder.val)
                root = holder.right
        return output
    
    def VLR(self, root: TreeNode): ## Preorder Traversal: center -> left -> right

        output = []
        stack = []
        
        while stack or root:
            if root:
                output.append(root.val)
                stack.append(root)
                root = root.left
            else:
                holder = stack.pop()
                root = holder.right
        return output


    def LRD(self, root: TreeNode): ## Postorder Traversal: left -> right -> center
        output = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                holder = stack[-1]
                if holder.right:
                    root = holder.right
                    holder.right = 0
                    holder.left = 0
                else:
                    stack.pop()
                    output.append(holder.val)
                
        return output
