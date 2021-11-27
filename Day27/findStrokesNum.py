
"""
The room is decorating, you would like to paint a skyline on the wall.
The skyline consists of rectangular buildings arranged in a line. The building are of the same width, but they may have different heights.
The skyline shape is given as an array A whose elements specify the heights of consecutive buildings. 

Ex:
    Given: [1,3,2,1,2,1,5,3,3,4,2]
Shape:
    [0,0,0,0,0,0,1,0,0,0,0] -> 1
    [0,0,0,0,0,0,1,0,0,1,0] -> 2
    [0,1,0,0,0,0,1,1,1,1,0] -> 2
    [0,1,1,0,1,0,1,1,1,1,1] -> 3
    [1,1,1,1,1,1,1,1,1,1,1] -> 1

Starting from the bottom, it can paint the skyline in horizontal stripes with 1, 3, 2, 2, 1 strokes per respective stripe
So, it should return 9.

Ex: 
    Given: [1,1,1,1]
It shold return 1

Solution: Given array A, it should return the sum of strokes. 

"""

def findStrokesNum(A):
    max_a = max(A)
    arr = []
    for i in range(1, max_a+1):
        pieces = 0
        connected = False
        for j in range(0, len(A)):
            if A[j] >= i:
                if connected:
                    continue
                else:
                    connected = True            
                    pieces += 1
            else:
                connected = False
        arr.append(pieces)
    print(arr)
    return sum(arr)


if __name__ == "__main__":
    print(findStrokesNum([1,3,2,1,2,1,5,3,3,4,2]))