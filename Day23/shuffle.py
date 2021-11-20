import random

"""
Demo of shuffling an array by randomly.
"""

def shuffle(arr):
    indices = [index for index in range(len(arr))]
    for i in range(random.randint(int(len(arr)/2), len(arr))):
        i = random.choice(indices)
        j = random.choice(indices)
        
        arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    print(shuffle([1,2,3,4,5,6]))