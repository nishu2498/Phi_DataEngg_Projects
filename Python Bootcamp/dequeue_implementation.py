import sys

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Deque:

    def __init__(self):
        self.front = None
        self.deque_size = 0

    def isEmpty(self):
        if self.deque_size == 0:
            return True
        return False

    def dequeLength(self):
        return self.deque_size

    def insertAtFront(self,item):
        temp = Node(item)

        if self.front == None:
            self.front = temp
            self.deque_size += 1
        else:
            temp.next = self.front
            self.front = temp
            self.deque_size += 1

    def insertAtRear(self,item):
        temp = Node(item)

        if self.front == None:
            self.front = temp
            self.deque_size += 1
        else:
            curr = self.front
            while curr.next!=None:
                curr = curr.next
            curr.next = temp
            self.deque_size += 1

    def deleteFromFront(self):
        try:
            if self.deque_size == 0:
                raise Exception("Deque is Empty")
            else:
                temp = self.front
                self.front = self.front.next
                self.deque_size -= 1
                del temp
        except Exception as e:
                print(str(e))

    def deleteFromRear(self):
        try:
            if self.deque_size == 0:
                raise Exception("Deque is Empty")
            else:
                curr = self.front
                prev = None
                while curr.next!=None:
                    prev = curr
                    curr = curr.next
                prev.next = curr.next
                self.deque_size -= 1
                del curr
        except Exception as e:
                print(str(e))

    def getfront(self):
        try:
            if self.deque_size == 0:
                raise Exception("Deque is Empty")
            else:
                return self.front.data
        except Exception as e:
            print(str(e))

    def getrear(self):
        try:
            if self.deque_size == 0:
                raise Exception("Deque is Empty")
            else:
                curr = self.front
                while curr.next!=None:
                    curr = curr.next
                return curr.data
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    d = Deque()

    d.insertAtFront(10)
    d.insertAtRear(20)
    d.insertAtFront(30)
    d.insertAtFront(40)
    d.insertAtRear(50)

    print(d.getfront())
    print(d.getrear())

    print(d.dequeLength())
    d.deleteFromRear()
    d.deleteFromFront()

    del Deque
    sys.exit(0)
main()
