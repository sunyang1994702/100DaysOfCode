"""
Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/
"""

def lengthOfLastWord(self, s: str) -> int:
    arr = s.split()
    i = 1
    while not arr[-i]:
        i += 1
    
    return len(arr[-i])
