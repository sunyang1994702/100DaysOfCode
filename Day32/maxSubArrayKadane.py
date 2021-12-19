"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Idea: following Kadane theroy. 
      Define current max and golbal max and searching from the second index. 
      
"""

def maxSubArray(nums):
    max_c, max_g = nums[0], nums[0]
    index = [0, 0]
    for i in range(1, len(nums)):
        max_c = max(nums[i], nums[i] + max_c)
        if max_c > max_g:
            max_g = max_c    
            
    return max_g


"""
Given an integer array nums,
find the contiguous subarray which has the largest sum and return its sum and subArray

"""
def returnMaxSubArray(nums):
    max_c, max_g = nums[0], nums[0]
    right = 0
    left = 0
    for i in range(1, len(nums)):
        if nums[i] >= nums[i] + max_c:
            left = i
            right = i
            max_c = nums[i]
        else:
            max_c = nums[i] + max_c

        if max_c > max_g:
            max_g = max_c
            right = i
        
    return max_g, nums[left:right+1]


if __name__ == '__main__':
    print(maxSubArray([5,4,-1,7,8]))
    print(returnMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]))