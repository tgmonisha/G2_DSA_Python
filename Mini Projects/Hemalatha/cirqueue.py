class CircQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            return False

        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = val
        return True

    def dequeue(self):
        if self.rear == -1:
            return None

        x = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return x

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Example usage:
circ_queue = CircQueue(int(input("Enter size of the queue: ")))

for i in range(12):
    print(circ_queue.enqueue(i))

print("DISPLAY:")
circ_queue.display()

for i in range(12):
    print(circ_queue.dequeue())

print("DISPLAY:")
circ_queue.display()

