"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Ex:
Input: nums=[2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement_1(nums):
    ## using hashmap
    ## Time complexity: O(n). But the space complexity: O(n)
    counts = {}
    
    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1
    
    return sorted(counts.items(), key=lambda d:d[1], reverse=True)[0][0]


def majorityElement_2(nums):
    ## Boyer-Moore
    ## Time complexity: O(n). But the space complexity: O(1)
    res, count = 0, 0
    for num in nums:
        if count == 0:
            res = num
            
        if num == res:
            count += 1
        else:
            count -= 1

    return res