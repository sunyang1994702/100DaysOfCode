"""
    Just a warm up coding practice by Python.
    The practice from Leetcode.
    Delete a node that was shown in the list
"""

def deleteNode(ListNode, node):
    temp = []
    for i in range(len(ListNode)):
        if ListNode[i] != node:
            temp.append(ListNode[i])
    return temp


if __name__ == '__main__':
    deleteNode([1,2,3,4,5,3,6], 3)