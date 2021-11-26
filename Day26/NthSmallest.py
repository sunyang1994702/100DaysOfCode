
"""
    ## arr was an unsorted array. m was a Nth smallest in this arr.
    ## mindset is just to find the right position of Nth smallest of arr comparing to the Nth.
"""

def NthSmallest(arr, m):

    while True:
        first_num = arr[0]
        small = []
        large = []
        for i in range(1, len(arr)):
            if arr[i] < first_num:
                small.append(arr[i])
            elif arr[i] > first_num:
                large.append(arr[i])
        small.append(first_num)
        
        if len(small) < m:
            arr = large
            m = m - len(small)
        elif len(small) > m:
            arr = small
        else:
            return small[-1]
            break


if __name__ == '__main__':
    print(NthSmallest([120, 3, 6,11, 79, 4, 10], 3))