#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


Numbers=np.array([3,14,16,17,21,22])
first=0;
last=len(Numbers)-1
Mid=int((first+last)/2)
flag=False
Num=int(input("Enter Number : "))

while (last>=first):
    Mid=int((first+last)/2)
    if(Numbers[Mid]==Num):
        flag=True
        break
    elif(Num>Numbers[Mid]):
        first=Mid+1
    elif(Num<Numbers[Mid]):
        last=Mid-1
        
if(flag):
    print("Numbers Found")
else:
    print("Not Found")


# In[ ]:




