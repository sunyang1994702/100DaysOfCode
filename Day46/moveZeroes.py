"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array. It means using O(1) space.
"""

## Quick Sort theory.
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    ## Quick Sort.
    
    l = 0
    for r in range(len(nums)):
        if nums[r]:            
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp

            l += 1
    return nums