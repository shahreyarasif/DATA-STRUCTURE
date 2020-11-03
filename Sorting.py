#!/usr/bin/env python
# coding: utf-8

#  # <center> Sorting </center>

# # Bubble Sort

# In[5]:


import numpy as np


# In[6]:


Array =np.array([100,99,1,3,2,4,25,64,82,-9,0])
n=len(Array)


# In[7]:


for i in range(0,n-1):
    for j in range(0,n-1-i):
        if(Array[j]>Array[j+1]):
            temp=Array[j]
            Array[j]=Array[j+1]
            Array[j+1]=temp
            
Array


# <h1> Selection Sort </h1>

# In[8]:


Numbers=np.array([10,9,8,7,6,5])
for i in range(0,len(Numbers)-1):
    index=i
    for j in range(i+1,len(Numbers)):
        if Numbers[j]<Numbers[index]:
            index=j 
    if Numbers[i] != Numbers[index]:
        temp=Numbers[i]
        Numbers[i]=Numbers[index]
        Numbers[index]=temp
        
        
print(Numbers)


# # Insertion Sort

# In[10]:


Numbers=np.array([1,67,43,11,58,6])
for i in range(1,len(Numbers)):
    temp=Numbers[i]  #8
    index=i       #2
    while(index !=0 and Numbers[index-1]>temp):
        Numbers[index]=Numbers[index-1]#
        index-=1
     
    Numbers[index]=temp
    
print(Numbers)

