"""
Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Time: O(n).
Space: O(n).
"""

def containsDuplicate(self, nums: List[int]) -> bool:
    ## using additional hash to store not exsited value
    nums_hash = set()
    for num in nums:
        if num in nums_hash:
            return True
        nums_hash.add(num)
    return False


if __name__ == "__main__":
    containsDuplicate([1,2,3,1])