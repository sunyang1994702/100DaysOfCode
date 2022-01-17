"""
Summary Ranges
Link: https://leetcode.com/problems/summary-ranges/
"""

def summaryRanges(self, nums: List[int]) -> List[str]:
               
    if not nums: return []
    start, cur, end = nums[0], nums[0], None
    output = []
    for n in nums[1:]:
        cur += 1
        if n == cur:
            end = n
        else:
            if not end:
                output.append(str(start))
            else:
                output.append(str(start) + "->" + str(end))
            start = n
            cur = n
            end = None
            
    if not end:
        output.append(str(start))
    else:
        output.append(str(start) + "->" + str(end))
            
    return output


if __name__ == '__main__':
    summaryRanges([0,2,3,4,6,8,9])