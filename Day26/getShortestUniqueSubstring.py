
"""
Given arr and str_, find all the shortest unique items of arr in str_.
"""



def getShortestUniqueSubstring(arr, str_):
    temp = []
  
    for i in range(0, len(str_)-len(arr) + 1):
        for j in range(0, len(arr)):
            if str_[i+j] in arr and not (str_[i+j] in temp):
                temp.append(str_[i+j])
            else:
                temp = []
                break
            
        if len(temp) == len(arr):
            return temp
            break


if __name__ == '__main__':
    print(getShortestUniqueSubstring(['x', 'y', 'z'], "dskxcnvslkadfoisdfaeisduxyzsdfwrwxndfnsjgflaskdfoi"))