"""
The problem is Given target and array contains integer only. 
Design an algorithm to find out the summation of all two available combination values in array is equal to target. 

Ex: arr = [1,2,3,5,7]. target = 5
Return [2,3]
"""

## This was traditional method by two dimentional loop. 
## The time complexity was O(n^2)
def isSumCombine(arr, target):
    results = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (arr[i] + arr[j]) == target:
                results.append([arr[i], arr[j]])
    return results


## Improve: Using hash map to run it by linear time. 
## The time complexity was O(n)
def isSumCombine_1(arr, target):
    c_hash = {}
    results = []
    for i in range(len(arr)):
        complement = target - arr[i]
        if arr[i] in c_hash:
            results.append([arr[c_hash[arr[i]]], arr[i]])
        else:
            c_hash[complement] = i
    return results if results else False


if __name__ == '__main__':
    print(isSumCombine([1,3,4,6,7], 7))
    print(isSumCombine_1([1,3,4,6,7], 10))