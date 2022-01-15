"""
Convert Sorted Array to Binary Search Tree.
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left, right = 0, len(nums)-1
        
        ## recrusively. 
        def func(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = func(l, mid-1)
            root.right = func(mid+1, r)
            return root
            
        return func(left, right)