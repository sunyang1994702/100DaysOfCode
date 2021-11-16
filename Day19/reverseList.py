"""
    Just a warm up coding practice by Python.
    The practice from Leetcode.
    Reverse a list.
"""


def reverseList(head):
    temp = []
    for i in range(len(head)-1, -1, -1):
        temp.append(head[i])
    return temp


if __name__ == '__main__':
    reverseList([1,2,3,4,5,3,6])