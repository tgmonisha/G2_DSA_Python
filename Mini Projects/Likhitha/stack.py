#CREATING STACK
class Stack:
     def __init__(self):           #declaring empty list
         self.items = []
         

     def isEmpty(self):            #check whether the stack is empty or not if it is empty it returns True otherwise False
         return self.items == []
         

     def push(self, item):         #Inserting items to the stack by using push operation
         self.items.append(item)
         print("pushed item: " + item)

     def pop(self):               #Removing an element from the stack by pop operation
         return self.items.pop()
         

     def peek(self):               #it gives top element in the stack
         return self.items[len(self.items)-1]
         

     def size(self):               #size of stack
         return len(self.items)
         

stack=Stack()
print(stack.isEmpty())
stack.push("10")
stack.push("stack")
stack.push("20.5")
stack.push("hello")
print("top of stack:",stack.peek())
print(stack.isEmpty())
print("size of stack:" ,stack.size())
print("popped item:" ,stack.pop())
print("size of stack:" ,stack.size())





#SAMPLE OUTPUT
"""True
pushed item: 10
pushed item: stack
pushed item: 20.5
pushed item: hello
top of stack: hello
False
size of stack: 4
popped item: hello
size of stack: 3
"""





