# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:48:37 2019

@author: SaurabhX360
"""

def Insert(t, val):
    nodecount = len(t)
    
    for element in t:
        if nodecount == 0:
            t.append(val)
        elif nodecount//2 == 1:
            InsertLeft(t, val)
        else:
            InsertRight(t, val)


def InsertLeft(t, val):
    t.append(val);
    t.append('')
    print(t)
    
def InsertRight(t, val):
    if t[-1] is None:
        t[-1] = val
    else:
        t.append(val)

def Len(x): 
    for element in x:
        return len(x) 

x=[]
y=['a']
z=['aa','bb']

Insert(x, 92)
Insert(x, 93)
Insert(y, 'b')
Insert(z, 'cc')
 
print (x, y, z)