# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:54:30 2019

@author: SaurabhX360
"""


class q:
  def __init__(self,qx,maxlen):
    self.qx = qx
    self.maxlen = maxlen
    self.f = 0
    self.r = 0
    for i in range(maxlen):
        myq.enq(None)
    
  def enq(self,n):
      print("start", self.f, self.r)
      if len(self.qx) == self.maxlen:
          if self.f == self.r:
              print("queue is full r=f, cannot enqueue")
          else:
              self.qx[self.r] = n
              self.r = (self.r + 1)%self.maxlen
          #return False
          #self.f+=1
          #self.qx[self.f] = n
      elif len(self.qx) < self.maxlen:
          self.qx.append(n)
          self.r = (self.r + 1)%self.maxlen
          #return True
      else:
          print("queue is greater than maxlen, cannot enqueue")
          #return False
      print("end", self.f, self.r)

  def dq(self):
      print("start", self.f, self.r)
      if len(self.qx) == 0:
          print("queue is empty with 0 elements, cannot deque")
      else:
          if len(self.qx) == self.maxlen:
              if self.r == self.f:
                  print("queue is empty, cannot dequeue")
                  return None
              else:
                  temp = self.qx[self.f]
                  self.qx[self.f] = None
                  self.f = (self.f+1)%self.maxlen
                  return(temp)
              
      print("end",self.f, self.r)

    #r = 0 ## next available cell
    #f = 0 ## first element of the queue
    ##enQ('a')
    ##print(qx)


myq = q([],4)
print(myq.dq())
for i in range(5):
    myq.enq(i*i)
print(myq.qx)
for i in range(5):
    print(myq.dq())
print(myq.qx)
for i in range(5):
    myq.enq(i*i)
print(myq.qx)
for i in range(5):
    print(myq.dq())
print(myq.qx)