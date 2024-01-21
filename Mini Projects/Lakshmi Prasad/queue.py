#queue
class queue:
  def __init__(self):
    self.que =[]
    self.rear = 0
  def enqueue(self,data):
    self.que.append(data)
    self.rear = data
  def dequeue(self):
    self.que.pop(0)
ls = queue()
ls.enqueue(1)
ls.enqueue(2)
ls.enqueue(3)
ls.enqueue(4)
ls.enqueue(5)
ls.dequeue()
print(ls.que)

output:
   [2, 3, 4, 5]
#circular queue
class cirque:
  def __init__(self):
    self.cique = []
    self.front = 0
    self.rear = 0
  def enque(self,data,n):
    if len(self.cique)<n:
      self.cique.append(data)
      self.rear = data
    else:
      print("circular queue is full")
  def dequeue(self):
    if self.front == self.rear:
      print('circular queue is full')
    else:
      self.cique.pop(1)
      self.front = self.cique[1]
lss = cirque()
lss.enque(1,5)
lss.enque(2,5)
lss.enque(3,5)
lss.enque(4,5)
lss.enque(5,5)
lss.enque(6,5)
print(lss.cique)
print(lss.front)
print(lss.rear)

output:
circular queue is full
[1, 2, 3, 4, 5]
0
5