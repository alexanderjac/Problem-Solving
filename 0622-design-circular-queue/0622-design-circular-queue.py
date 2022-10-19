class MyCircularQueue:
    """
     cQ = [] 
     dequeue = cQ.pop(0)
     lptr. = 0
     rptr = 2 < 3
     cQ = [5,1, 4,2,3]
                ^
                    ^
     len_ = -1 
        
    """

    def __init__(self, k: int):
        self.k = k
        self.circularQueue = [0 for i in range(k)]
        self.length = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.length>=self.k:
            return False
        if self.rear +1 ==self.k:
            self.rear = 0
        else:
            self.rear +=1
        print(self.rear)
        self.circularQueue[self.rear] = value
        self.length +=1
        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        if self.front+1 == self.k:
            self.front = 0
        else:
            self.front +=1
        self.length -=1
        return True

    def Front(self) -> int:
        if self.length>=1:
            return self.circularQueue[self.front]
        return -1

    def Rear(self) -> int:
        if self.length>=1:
            return self.circularQueue[self.rear]
        return -1
    def isEmpty(self) -> bool:
        return self.length ==0

    def isFull(self) -> bool:
        return self.length ==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()