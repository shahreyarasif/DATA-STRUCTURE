#!/usr/bin/env python
# coding: utf-8

# In[5]:


from numpy import array
Arr=array([3,2,1,6,9,4,7,8])

Count=array([0 for i in range(10)])

for i in range(len(Arr)):
    Count[Arr[i]]+=1

for i in range(1,len(Count)):
    Count[i]+=Count[i-1]
    

SArray=array([0 for i in range(len(Arr))])

for i in range(len(Arr)):
    SArray[Count[ Arr[i] ]-1]=Arr[i] #Arr[3]=1 #Count[3]=2 [2-1]=1
    Count[Arr[i]]-=1
    

print(SArray)


# In[7]:





# In[ ]:





# In[ ]:





# In[ ]:




