"""
small demo judge if the arr is a palindrome
"""


def isPalindrome(head):
    i = 0
    count = 0
    head_len = len(head)    
    while i <= (head_len/2):
        if head[i] == head[head_len-i-1]:
            i += 1
            count = 1
        else:
            count = 0
            break
    
    if count == 1:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    isPalindrome([1,2,3,4,5,4,3,2,1])
