# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.current_min_index = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min_index == None:
            self.current_min_index = 0
        elif val < self.stack[self.current_min_index]:
            self.current_min_index = len(self.stack) - 1
        self.min_stack.append(self.current_min_index)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        current_min = self.stack[self.current_min_index]
        item = self.stack.pop()
        self.min_stack.pop()
        if item == current_min and len(self.min_stack) > 0:
            self.current_min_index = self.min_stack[len(self.min_stack) - 1]
        return item

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        item = self.stack[self.current_min_index]
        return item



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
