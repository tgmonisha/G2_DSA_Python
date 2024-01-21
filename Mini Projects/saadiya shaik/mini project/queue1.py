# Initialize an empty queue as a list
queue = []

# Adding items to the queue (enqueue)
queue.append(89)
queue.append(29)
queue.append(39)

# Deleting items from the queue (dequeue)
if len(queue) > 0:
    item = queue.pop(0)
    print(f"Dequeued: {item}")
else:
    print("Queue is empty")

# Now the queue contains [2, 3]

