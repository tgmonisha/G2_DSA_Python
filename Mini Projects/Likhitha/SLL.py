#SINGLY LINKED LIST 
class Node:   #Creating class node
	def __init__(self,data):
		self.data=data
		self.ref=None 
class SinglyLinkedList:  	#Creating linked list class
	def __init__(self):
		self.head=None
	def print_LinkedList(self):
		if(self.head==None):
			print("Linked list is empty")
		else:
			n=self.head
			while n!=None:
				print(n.data,"-->",end="")
				n=n.ref
	def add_beginning(self,data):   #inserting of a node at the beginning of the linked list
		new_node=Node(data)
		new_node.ref=self.head
		self.head=new_node
	def append(self,data):    #inserting of a node at the ending of the linked list
		new_node=Node(data)
		if(self.head==None):
			self.head=new_node
		else:
			n=self.head
			while(n.ref is not None):
				n=n.ref
			n.ref=new_node
	def add_after_node(self,data,x):    #inserting a node after the specified node of the linked list
		n=self.head
		while(n!=None):
			if(x==n.data):
				break
			n=n.ref
		if(n is None):
			print("node is not present in linked list")
		else:
			new_node=Node(data)
			new_node.ref=n.ref
			n.ref=new_node
	def add_before_node(self,data,x):    #inserting a node before the specified node of the linked list
		if(self.head is None):
			print("linked list is empty")
			return
		if(self.head.data==x):
			new_node=Node(data)
			new_node.ref=self.head
			self.head=new_node
			return
		n=self.head
		while(n.ref is not None):
			if(n.ref.data==x):
				break
			n=n.ref
		if(n.ref is None):
			print("Node is not found")
		else:
			new_node=Node(data)
			new_node.ref=n.ref
			n.ref=new_node
	def delete_beginning(self):    #deleting the beginning node of the linked list
		if(self.head is None):
			print("we cant delete node beacuse linked list is empty")
		else:
			self.head=self.head.ref
	def delete_end(self):     #deleting the ending node of the linked list
		if(self.head is None):
			print("we cant delete node because linked list is empty")
		elif(self.head.ref is None):
			self.head=None
		else:
			n=self.head
			while(n.ref.ref is not None):
				n=n.ref
			n.ref=None
	def delete_by_value(self,x):  #deleting the specified node present in a linked list
		if(self.head is None):
			print("we cant delete node beacuse linked list is empty")
			return
		if(x==self.head.data):
			self.head=self.head.ref
			return
		n=self.head
		while(n.ref is not None):
			if(x==n.ref.data):
				break
			n=n.ref
		if(n.ref is None):
			print("Node is not present")
		else:
			n.ref=n.ref.ref
LL1=SinglyLinkedList()
LL1.add_beginning(30)
LL1.add_beginning(20)
LL1.add_before_node(10,20)
LL1.add_after_node(40,30)
LL1.append(100)
LL1.append(120)
LL1.add_beginning(130)
LL1.delete_beginning()
LL1.delete_end()
LL1.delete_by_value(100)
LL1.print_LinkedList()



