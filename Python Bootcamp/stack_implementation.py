import sys

class Stack:
    def __init__(self):
        self.L = []

    def push(self,new_data):
        self.L.append(new_data)

    def top(self):
        if len(self.L) == 0:
            return None
        return self.L[-1]

    def pop(self):
        if len(self.L) == 0:
            return None
        data = self.L[-1]
        del self.L[-1]
        return data

    def is_empty(self):
        return len(self.L) == 0

    def peek(self):
        return self.L[0]

    def size(self):
        return len(self.L)

if __name__ == '__main__':
    stack = Stack()
    if stack.is_empty():
        print("Stack is empty")
    data = stack.top()
    if data is None:
        print("cannot top an empty stack")
    data = stack.top()
    if data is None:
        print("cannot pop an empty stack")
    for x in range(1,11):
        stack.push(x)

    data = stack.top()
    print("Top element: ",data)

    data = stack.peek()
    print("Peek element: ",data)

    print("Size of stack: ",str(stack.size()))

    while stack.is_empty()!=True:
        data = stack.pop()
        print("Poped data: ",data)

    del stack
    sys.exit(0)
main()
