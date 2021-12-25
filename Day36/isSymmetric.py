"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Ex: root = [1,2,2,3,4,4,3]
            1
          2   2
       3   4 4  3
Output: True
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_1:
    ## Recrusive solution. Time complexity: O(2^n) 
    def isSymmetric(self, root):
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)        
        
    def isMirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)
        return leftroot == rightroot


class Solution_2:
    ## Iterative solution. Time complexity: O(n)
    def isSymmetric(self, root):
        if root is None:
            return True
        
        q1 = [root.left]
        q2 = [root.right]
        while q1 and q2:
            l, r = q1[0], q2[0]
            del q1[0]
            del q2[0]
            
            if (l is not None and r is None) or (l is None and r is not None):  
                return False
                
            if l or r:        
                if l.val == r.val:
                    q1.append(l.left)
                    q1.append(l.right)
                    q2.append(r.right)
                    q2.append(r.left)
                else:
                    return False
        return True