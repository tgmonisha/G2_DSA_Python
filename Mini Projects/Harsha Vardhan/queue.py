queue = []


def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")


def dequeue():
    if queue:
        item = queue.pop(0)
        print(f"Dequeued: {item}")
    else:
        print("Queue is empty")


while True:
    print("Queue:", queue)
    print("Options:")
    print("1. Add an item")
    print("2. Delete an item")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        enqueue(item)
    elif choice == "2":
        dequeue()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
