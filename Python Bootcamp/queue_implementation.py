import sys

class Queue:

    def __init__(self,size):
        self.L = [None]*size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0

    def DeQueue(self):
        if self.isEmpty():
            print("Queue Underflow!! Terminating process..")
            exit(1)
        value = self.L[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return value

    def EnQueue(self,item):
        if self.isFull():
            print("Overflow!! Terminating process..")
            exit(1)
        self.rear = (self.rear + 1) % self.capacity
        self.L[self.rear] = item
        self.count = self.count + 1

    def peek(self):
        if self.isEmpty():
            print("Queue Underflow!! Terminating process..")
            exit(1)
        return self.L[self.front]

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity
    
if __name__ == '__main__':
    q = Queue(10)
    if q.isEmpty():
        print("Queue is empty")
    fvalue = q.front
    if fvalue is None:
        print("Cannot print front of empty queue")
    rvalue = q.rear
    if rvalue is None:
        print("Cannot print rear of empty queue")

    for x in range(0,8):
        q.EnQueue(x)
    print("Queue Front " + str(q.front))
    print("Queue Rear " + str(q.rear))

    print("Size of Queue: ",q.size())
    while q.isEmpty() != True:
        value = q.front
        q.DeQueue()
        print("DeQueued value: ",value)

    del Queue
    sys.exit(0)
main()
