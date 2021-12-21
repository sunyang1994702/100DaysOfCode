"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

## Method1: Brute Force. Time complexity: O(2^n)

## Ex. n = 4
##      0
##    1   2
##   2 3 3 4
## 34 4 4 
##4
def numOfWaysClimbingStairs_BF(n):
    if n == 0 or n == 1:
        return 1
    else:
        return numOfWaysClimbingStairs_BF(n-1) + numOfWaysClimbingStairs_BF(n-2)


## Method2: Dynamic Programming. Time complexity: O(n)
## Idea: using bottom-up, storing each calculated data. So for the cases of duplicated data, just extract data from storage. 

def numOfWaysClimbingStairs_DP(n):
    first = 1
    second = 1
    for i in range(n-1):
        temp = first
        first = first + second
        second = temp

    return first


if __name__ == '__main__':
    numOfWaysClimbingStairs_BF(10)
    numOfWaysClimbingStairs_DP(10)