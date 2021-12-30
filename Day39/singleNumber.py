"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Ex: Input: nums = [2,2,1]
    Output: 1
"""


def singleNumber(nums):
    nums_hash = {}
    for i in range(len(nums)):
        if nums[i] in nums_hash:
            nums_hash[nums[i]] += 1
        else:
            nums_hash[nums[i]] = 1
    

    return list(nums_hash.keys())[list(nums_hash.values()).index(1)]


"""
Using bitwise operation ^

4: 0100
1: 0001

4^1 : 0101=5

60 = 0011 1100 
13 = 0000 1101 

60^13 = 0011 0001 = 49

"""

def singleNumber_2(nums):
    res = 0
    for num in nums:
        res ^= num
        
    return res
