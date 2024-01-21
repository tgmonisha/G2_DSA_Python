class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index out of range.")
            return

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            print("Index out of range.")
            return

        new_node.next = current.next
        current.next = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print("Key not found in the linked list.")
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main_loop():
    linked_list = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Display Linked List")
        print("2. Prepend a value")
        print("3. Insert at index")
        print("4. Append a value")
        print("5. Delete a value")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Linked List:")
            linked_list.display()
        elif choice == "2":
            value = int(input("Enter a value to prepend: "))
            linked_list.prepend(value)
        elif choice == "3":
            index = int(input("Enter the index to insert at: "))
            value = int(input("Enter a value to insert: "))
            linked_list.insert_at_index(index, value)
        elif choice == "4":
            value = int(input("Enter a value to append: "))
            linked_list.append(value)
        elif choice == "5":
            value = int(input("Enter a value to delete: "))
            linked_list.delete(value)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


main_loop()
