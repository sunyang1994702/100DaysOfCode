"""
Pascal's Triangle 2
Link: https://leetcode.com/problems/pascals-triangle-ii/
"""

def getRow_1(self, rowIndex: int) -> List[int]:
    res = [1]
    for i in range(1, rowIndex+1):
        ## add 1 in behind of each res
        res.append(1)
        # left-right direction.
        temp1 = 1
        for j in range(1, i):
            temp = res[j]
            res[j] = res[j] + temp1
            temp1 = temp
    return res


def getRow_2(self, rowIndex: int) -> List[int]:
    res = [1]
    for i in range(1, rowIndex+1):
        ## add 1 in behind of each res
        res.append(1)
        # right-left direction.
        for j in range(1, i):
            index = len(res) - 1
            res[index-j] = res[index-j] + res[index-j-1]
    return res











                