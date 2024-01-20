class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linked_list:
  def __init__(self):
    self.head = None
  def prepend(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head=new_node
  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    temp = self.head
    while(temp.next != None):
        temp= temp.next
    temp.next= new_node
  def insert_pos(self,data,pos):
    new_node = Node(data)
    temp= self.head
    count = 0
    if self.head == None:
      self.head = new_node
    elif self.head!=None and count< pos-1:
      temp = temp.next
      count+=1
    new_node.next=temp.next
    temp.next=new_node
  def delete(self):
    temp = self.head
    while(temp.next.next is not  None):
      temp = temp.next
    temp.next = None
  def delete_at_first(self):
    temp = self.head.next
    self.head= temp
  def delete_at_pos(self,pos):
    temp = self.head
    count =0
    while temp and count<pos-1:
      temp = temp.next
      count+=1
    temp.next = temp.next.next 
    
  def display(self):
    temp = self.head
    while(temp):
      print(temp.data,"-->",end=" ")
      temp=temp.next





ls = Linked_list()
ls.prepend(3)
ls.prepend(2)
ls.prepend(1)
ls.append(6)
ls.insert_pos(4,3)
ls.delete()
ls.delete_at_first()
ls.delete_at_pos(1)
ls.display()
  