#creation of stack
class stack:
    def __init__(self):
        stack.elements=[]           
# Checking for empty stack
    def isEmpty(self):
        return stack.elements==[]
#inserting items into the stack
    def push(self, n):
        self.elements.append(n)
        print("pushed element:" +n)
# Removal of an element from the stack
    def pop(self):
            return self.elements.pop()
#top of the stack
    def peek(self):
        return self.elements[len(self.elements)-1]
#size of the stack
    def size(self):
        return len(self.elements)
stack=stack()
stack.push("10")
stack.push("20")
stack.push("30")
print("top of the stack:",stack.peek())
print("size of the stack:",stack.size())
print(stack.pop())
print(stack.pop())
print(stack.pop())

