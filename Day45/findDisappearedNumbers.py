"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Important: O(n) time complexity. O(1) space complexity.
"""

## Method_1: using set.
def findDisappearedNumbers_1(nums):        
    arr_1 = set([i for i in range(1, len(nums)+1)])
    arr_2 = set(nums)
    return list(arr_1-arr_2)

## Method_2: Regard number of array as an index. 
## nums = [4,3,2,7,8,2,3,1]. First value is 4. So the 4th postion value would be minus 7 and keep going.
## array        [4,3,2,7,8,2,3,1]
## mark minus    - - - -     - -  
## position      1 2 3 4 5 6 7 8
## We can see the values in 5th and 6th posion are positive. So return 5 and 6 which didn't show in the raw array.
def findDisappearedNumbers_2(nums):
    for num in nums:
        num = abs(num)
        if nums[num-1] > 0:
            nums[num-1] = -nums[num-1]
    
    return [i+1 for i in range(len(nums)) if nums[i] > 0]