#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
A=np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]])
A


# In[11]:



Count1=0
Diagonal=0
Count2=0
lowerdiagonal=0
Upperdiagonal=0
sum=0
for i in range(4):
    for j in range(4):
        if(i==j):
            Count1+=1
            Diagonal+=A[i,j]
for i in range(4):
    for j in range(4):
        if(i>=1 and j<i):
            Count2+=1
            lowerdiagonal+=A[i,j]
for i in range(4):
    for j in range(4):
        if(j>i):
            Upperdiagonal+=A[i,j]
            
for i in range(4):
    for j in range(4):
        temp=i+j
        if(temp%2==0):
            sum+=A[i,j]
print(A)
print("Diagonal",Diagonal/Count1)
print("Lower Diagonal Mean",lowerdiagonal/Count2)
print("Upper Diagonal Mean",Upperdiagonal/Count2)
print("Sum of ij that is divisible by 2",sum)


# In[ ]:




