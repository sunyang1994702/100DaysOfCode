"""
Merge two sorted lists. 
"""

def mergeTwoLists(l1, l2):
    short_arr = []
    long_arr = []
    if len(l1) > len(l2):
        long_arr = l1
        short_arr = l2
    else:
        long_arr = l2
        short_arr = l1

    s_i = 0
    l_i = 0
    temp = []
    while True:
        try:
            if long_arr[l_i] < short_arr[s_i]:
                temp.append(long_arr[l_i])
                l_i += 1
            elif long_arr[l_i] > short_arr[s_i]:
                temp.append(short_arr[s_i])
                s_i += 1
            else:   
                temp.append(long_arr[l_i])
                temp.append(short_arr[s_i])
                l_i += 1
                s_i += 1
        except:
            temp = temp + short_arr[s_i:] + long_arr[l_i:]
            break
            
    return temp


if __name__ == '__main__':
    print(mergeTwoLists([1,2,4,5,6,7], [3,4,5,6,10,11,12,14]))