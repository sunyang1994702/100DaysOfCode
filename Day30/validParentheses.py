"""
An algorithm for checking if given string is a valid parentheses string following rules below:
1,Open brackets must be closed by the same type of brackets.--> () [] {}
2,Open brackets must be closed in the correct order. --> () OK. )( is NG.

Core Idea: 
    1, using hash map to store parentheses pairs
    2, Delete one pairs for valid parentheses once found it until you traverse the whole string. 
"""



def isValid(s: str):
    dict_brackets = {"(":")", "{":"}", "[":"]"}
    i = 0
    while len(s) > 1 and i < len(s)-1 and s[i] in dict_brackets:
        if dict_brackets[s[i]] != s[i+1]:
            i += 1
        else:
            s = s.replace(s[i]+s[i+1], "")
            i = 0
    
    return False if s else True


if __name__ == '__main__':
    print(isValid("(([]){})"))