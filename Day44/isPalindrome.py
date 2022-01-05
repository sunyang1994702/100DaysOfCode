"""
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    ## Using array, O(n) time and O(n) space
    def isPalindrome_n_space(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
                
        return True
    
    ## Using two pointers. slow and fast. O(n) time and O(1) space
    def isPalindrome_1_space(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the rest of array. 
        # Ex: [1,2,3,2,1]. Currently, slow is at index of 3. 1->2->3
        # What need to do is to reverse rest of array. None<-3<-2<-1.
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # judge the if palindrome
        # Similarily, using left and right pointers. 
        left, right = head, prev
        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
                continue
            else:
                return False
        return True