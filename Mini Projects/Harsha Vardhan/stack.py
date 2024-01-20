class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. No top element.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def main_loop():
    stack = Stack()

    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if stack is empty")
        print("5. Get stack size")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value to push: ")
            stack.push(value)
        elif choice == "2":
            popped_item = stack.pop()
            if popped_item is not None:
                print("Popped item:", popped_item)
        elif choice == "3":
            top_element = stack.peek()
            if top_element is not None:
                print("Top element:", top_element)
        elif choice == "4":
            print("Is stack empty?", stack.is_empty())
        elif choice == "5":
            print("Stack size:", stack.size())
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
main_loop()

