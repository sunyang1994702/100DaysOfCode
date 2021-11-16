"""
    Just a warm up coding practice by Python.
    The practice from Leetcode.
    Delete nth node that was shown in the list
"""



def removeNthFromEnd_1(head, n):
    temp = []
    for i in range(len(head)):
        if i == (len(head)-n):
            continue
        temp.append(head[i])
    return temp


if __name__ == '__main__':
    removeNthFromEnd_1([1,2,3,4,5,3,6], 3)