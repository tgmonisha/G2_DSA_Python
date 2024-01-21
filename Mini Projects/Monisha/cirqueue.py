class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is emptywe Can't dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        if self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()


# Create a circular queue with a capacity of 5
cq = CircularQueue(5)

# Enqueue elements
cq.enqueue(78)
cq.enqueue(23)
cq.enqueue(30)
cq.enqueue(84)
cq.enqueue(65)

# Display the queue
cq.display()  

# Dequeue elements
item = cq.dequeue()
print(f"Dequeued: {item}")  

item = cq.dequeue()
print(f"Dequeued: {item}") 



# Display the queue
print("After dequeue operation the items in queue are:")
cq.display() 

