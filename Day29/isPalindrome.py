"""
    Find all single longest sub Palindrom array in the given array. 
    Ex: [1,2,3,2,1,2]
    return [1,2,3,2,1], [2,1,2]
    The [2,3,2] has alrady exsited in [1,2,3,2,1]. So no need to return it again.
"""

def subPalindrom(arr):
    results = []
    for i in range(len(arr)):
        ## odd length:  aba
        l, r = i-1, i+1
        subArr = []     
        while l >= 0 and r < len(arr) and arr[l] == arr[r]:
            if (r - l + 1) > len(subArr):
                subArr = arr[l:r+1]
            l -= 1
            r += 1
        if subArr:
            results.append(subArr)
            
        ## even length:  abba
        l, r = i, i+1
        subArr = []     
        while l >= 0 and r < len(arr) and arr[l] == arr[r]:
            if (r - l + 1) > len(subArr):
                subArr = arr[l:r+1]
            l -= 1
            r += 1
        if subArr:
            results.append(subArr)
    return results


if __name__ == "__main__":
    print(subPalindrom([1,2,3,4,3,2,1,2,14,2,2,14,19,200]))