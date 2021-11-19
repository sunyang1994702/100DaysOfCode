"""
    array_1 : nums1, m
    array_2 : nums2, n
    merge first mth of nums1 and first nth of nums2 and sorted.

"""


def merge_1(nums1, m, nums2, n):
    i = 0
    j = 0
    temp = []
    
    nums1 = sorted(nums1[0:m])
    nums2 = sorted(nums2[0:n])
    
    while i < m and j < n :
        if nums1[i] < nums2[j]:
            temp.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            temp.append(nums2[j])
            j += 1
        else:   
            temp.append(nums1[i])
            temp.append(nums2[j])
            i += 1
            j += 1
    temp = temp + nums1[i:m] + nums2[j:n]
    return temp


if __name__ == '__main__':
    print(merge_1([6,2,3,0,0,0], 4, [2,5,6], 3))