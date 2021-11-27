
"""
An array A consisting of N integers. triplet of indices (P,Q,R) is called a triangle if 0 <= P < Q < R < N and:
A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q],

Ex: a given array A = [10, 2, 5, 1, 8, 20]
Triplet (0, 2, 4) is a traingle and its perimeter equals 10+5+8=23. There is no other triangle in this array with a larger perimeter.

"""



def findLargestTraingle(A):
    A = sorted(A, reverse=True)
    for i in range(0, len(A)-2):
        for j in range(i+1, len(A)-1):
            for z in range(j+1, len(A)):
                if A[i] < A[j] + A[z]:
                    return A[i] + A[j] + A[z]
    return -1


if __name__ == "__main__":
    print(findLargestTraingle([10, 2, 5, 1, 8, 20]))