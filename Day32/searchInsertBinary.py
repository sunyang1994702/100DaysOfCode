"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

runtime complexity: O(n)

"""

def searchInsert(nums, target):
    i = 0
    signal = True
    while signal and i < len(nums):
        if target > nums[i]:
            i += 1
        else:
            if target <= nums[i]:
                signal = False
    return i

"""
runtime complexity: O(log n)
Idea: using binary tree
"""

def searchInsertBinary(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        center = (l+r) // 2

        if target == nums[center]:
            return center

        if target > nums[center]:
            l = center + 1
        else:
            r = center - 1

    return l

"""
Take a look at algorithm about binary tree.
Find a target value if it's in a given array.
If return the value and index
If not return False.

Idea: Just define two pointers, left and right. Find through center of array. 
      If target is larger than value in center, then shift (center+1) index to the left pointer (Just searching right part only for next loop). 
      If target is smaller than value in center, then shift (center-1) index to the right pointer (Just searching left part only for next loop). 
"""

def binarySearch(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        center = (l+r) // 2
        if target == nums[center]:
            return center, nums[center]
        
        if target > nums[center]:
            l = center + 1
        else:
            r = center - 1
        
    return False


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 4))
    print(searchInsertBinary([1,3,5,6], 4))
    print(binarySearch([1,3,5,6,10,13,45,100], 45))