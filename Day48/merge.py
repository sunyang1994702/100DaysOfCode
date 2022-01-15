"""
A demo from Leetcode about merge two sorted array.
Link: https://leetcode.com/problems/merge-sorted-array/
"""

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last = m + n -1
    ## merge in nums1 starting from right side.
    while m > 0 and n > 0:
        if nums2[n-1] > nums1[m-1]:
            nums1[last] = nums2[n-1]
            n -= 1
        else:
            nums1[last] = nums1[m-1]
            nums1[m-1] = 0
            m -= 1
        last -= 1
    
    ## fille nums1 with leftover nums2 elements
    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1
    
merge([1,2,3,0,0,0], 3, [2,5,6], 3)