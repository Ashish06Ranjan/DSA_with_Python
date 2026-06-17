"""

Problem : 155. Min Stack 
Approach :  Use two stacks:
              stack → stores all elements.
              minStack → stores the minimum element seen so far at each position.
            While pushing:
              Add the value to stack.
              Add the smaller value between the current element and the current minimum to minStack.
            While popping:
              Remove the top element from both stacks.
            For top():
              Return the top element of stack.
            For getMin():
              Return the top element of minStack, which always stores the current minimum.

"""
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
