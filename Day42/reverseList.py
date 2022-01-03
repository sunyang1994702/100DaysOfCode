"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Ex:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList_1(self, head):
        ## Iteratively. Using two pointers.
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev


    def reverseList_2(self, head):
        ## Recrusively. 
        if not head:    
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList_2(head.next)
            head.next.next = head
            
        head.next = None
        
        return newHead

    