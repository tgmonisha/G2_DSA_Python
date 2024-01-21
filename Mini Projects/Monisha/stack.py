class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("None")

stack = LinkedListStack()

stack.push(50)
stack.push(30)
stack.push(40)

print("values in Stack :")
stack.display()

print("Peek:", stack.peek())

popped = stack.pop()
print("Popped:", popped)

print("values in Stack after pop:")
stack.display()

