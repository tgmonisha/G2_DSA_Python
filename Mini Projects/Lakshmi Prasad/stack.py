class stack:
  def __init__(self):
    self.sta=[]
  def push(self,data):
    self.sta.append(data)
  def remove(self):
    self.sta.pop()
  def display(self):
    for i in self.sta[::-1 ]:
      print(i)
  def peak(self):
    if len(self.sta) is not None:
      return self.sta[-1]
    else:
      print("stack is empty")
  def isempty(self):
    if len(self.sta) is None:
      return True
    else:
      return False
  def issize(self):
    if len(self.sta) is not None:
      return(len(self.sta))
    else:
      return False



st = stack()
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.push(7)
st.remove()
st.display()
print("peak of the stack is",st.peak())
print("stack is empty:",st.isempty())
print("length os th stack is",st.issize())