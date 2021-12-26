"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

I will show three solutions Recrusive, Breadth-First Search iterative, Depth-First Sesarch iterative.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        ## recrusive solution
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 


    def BFS(self, root):
        ## Breadth-First Search. using queue FIFO
        if root is None:
            return 0
        
        queue = [root]
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                del queue[0]
                
            level += 1
        return level
    

    def DFS(self, root):
        ## Depth-First Search. using stack LIFO
        if root is None:
            return 0
        
        stack = [(root, 1)]
        res = 1
        
        while stack:
            node, depth = stack.pop()

            res = max(res, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))

        return res

    """
    One more questions: Return maximum breadth of this tree.
    """
    def maxBreadth(self, root):
        ## Based on BFS. 
        if root is None:
            return 0
        
        queue = [root]
        output = [1]
        level = 0
        while queue:
            level += 1
            node_len = 0
            for i in range(len(queue)):
                node = queue[0]
                if node.left:
                    queue.append(node.left)
                    node_len += 1
                if node.right:
                    queue.append(node.right)
                    node_len += 1
                    
                del queue[0]
            output.append(node_len)
        return max(output)