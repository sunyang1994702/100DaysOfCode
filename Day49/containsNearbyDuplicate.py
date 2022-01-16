"""
Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/

Two method
1. Brute force
2. Hash map
"""


# Brute force. Time: O(n^2)
def containsNearbyDuplicate_1(self, nums: List[int], k: int) -> bool:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if abs(i-j) <= k and nums[i] == nums[j]:
                return True
    return False


# Hash map. Time: O(n)
def containsNearbyDuplicate_2(self, nums: List[int], k: int) -> bool:
    nums_hash = {}
    for i in range(len(nums)):
        if nums[i] in nums_hash and (i - nums_hash[nums[i]]) <= k:
            return True
        nums_hash[nums[i]] = i
    return False
                    

if __name__ == '__main__':
    containsNearbyDuplicate_2([1,2,3,1], 3)