
"""
Demo of adding value in an array and call a function get minimum value. Run in one-time O(1).
"""

class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]
    
    def show(self):
        return self.stack


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(10)
    minStack.push(5)
    minStack.push(2)
    minStack.push(4)
    print(minStack.getMin())