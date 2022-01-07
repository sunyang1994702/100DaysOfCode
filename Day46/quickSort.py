
"""
A demo about quick sort! 

1. select a random value as pivot element. Normally the first position value.
2. put the values less than pivot in the left side. and values bigger than pivot in the right side.
3. Run both side using the same rules of step 1 and 2 recursively.

"""

def sortFun(nums, left, right):

    if left >= right:
        return
    # the value in leftmost position is pivot value. 
    pivot = nums[left]
    l = left
    r = right
    while l < r:
        ## move the right index
        while nums[r] >= pivot:
            r -= 1
        ## move the left index
        while nums[l] <= pivot:
            l += 1
        
        if l < r:
            ## swap the left and right index value when satisfy the condition.
            nums[l], nums[r] = nums[r], nums[l]
    
    ## swap the right value and pivot value. 
    nums[left], nums[r] = nums[r], nums[left]

    ## recrusively sorting the left set
    sortFun(nums, left, r-1)
    # recrusively sorting the right set
    sortFun(nums, r+1, right)

    return nums


def quickSort(nums):
    ## define two pointers left and right
    l, r = 0, len(nums)-1
    print(sortFun(nums, l, r))


quickSort([6,1,2,7,9,3,4,5,10,8])


### ryo.okada@capgemini.com



