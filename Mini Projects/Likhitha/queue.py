# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Adding of an element
    def enqueue(self, item):
        self.queue.append(item)

    # Removing an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Displaying  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
q = Queue()
q.enqueue("hi")
q.enqueue("hello")
q.enqueue("how")
q.enqueue("are")
q.enqueue("you?")
q.display()
q.dequeue()
print("After removing an element")
q.display()


#Circular Queue Implementation
#CircularQueue class
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
            return

        # If queue is empty
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        # Check if queue is empty
        if self.front == -1:
            print("Queue is empty!")
            return

        # If this is the last element
        if self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        temp = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        return temp

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
cq = CircularQueue(6)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print("Queue after enqueues:")
cq.display()
cq.dequeue()
print("Queue after dequeues:")
cq.display()
cq.enqueue(60)
cq.enqueue(70)
print("Queue after some more enqueues:")
cq.display()









