#!/usr/bin/env python
# coding: utf-8

# # Simple Linked List

# In[1]:


class Node:
    def __init__(self,data):
        self.Info=data
        self.Next=None;
    def Print(self):
        print(self.Info)
        if(self.Next is not None):
            self.Next.Print()

Start=Node(22)
Start.Next=Node(24)
Start.Next.Next=Node(25)
Start.Next.Next.Next=Node(26)

        


# In[27]:


Start.Print()


# # Linked List By Using OOP

# In[2]:


class node:
    def __init__(self,value):
        self.Info=value
        self.Next=None
        
    def Print(self):
        print(self.Info)
        if(self.Next is not None):
            self.Next.Print()
            
class linkedlist:
    
    
    def __init__(self,value):
        self.Start=node(value)
    def Print(self):
        if self.Start==None:
            print('empty list')
        else: 
            self.Start.Print()
        
    def inertatBegnning(self,value):
        if(self.Start==None):
            self.Start=Node(value)
            
        else:
            temp=node(value)
            temp.Next=self.Start
            self.Start=temp        
    def insertatend(self,value):
        if(self.Start is None):
            self.Start=node(value)
            
        else:
            ptr=self.Start
            while(ptr.Next != None):
                ptr=ptr.Next
            ptr.Next=node(value)
            
    def Count(self):
        if(self.Start is None):
            print("list is empty")
        else:
            ptr=self.Start
            count=1
            while(ptr.Next !=None):
                ptr = ptr.Next
                count+=1
        return count
    def InsertionPostion(self,Position,value):
        if(Position==1):
            self.InsertatBegin(value)
        elif (Position > 1 and Position <= self.Count() + 1):
            ptr=self.Start
            for i in range(1,Position -1):
                ptr = ptr.Next
            New=node(value)
            New.Next=ptr.Next
            ptr.Next=New
        else:
            print("position not found in list")
            
    def Search(self, value):
        if (self.Start is None):
            print("List is Empty")
        else:
            ptr = self.Start
            count = 1
            while(ptr != None and ptr.Info != value):
                ptr = ptr.Next
                count += 1
        
        if(ptr == None):
            print(f"value {value} Not found is List")
        else:
            print(f"value {ptr.Info} found on position {count}")
            
    def insertafter(self,find,value):
        if(self.Start==None):
            print('list is empty')
            
        elif (self.Search(find) >=0):
            self.InsertionPostion(self.Search(find)+1,value)
        else:
            print('position not found')
    
    def InsertBefore(self,find,value):
        if(self.Start==None):
            print("list is empty")
        elif(self.Search(find) >=0):
            self.InsertionPosition(self.Search(find))
        else:
            print("position not found")
            
    def changevalue(self,find,value):
        if (self.Start==None):
            print('list is empty')
        else:
            ptr=self.Start
            while (ptr!=None and ptr.Info!=find):
                ptr=ptr.Next
                
        if (ptr==None):
            print(f"value {find} Not found is List")
        else:
            ptr.Info=value
            print(f'value{find} has been changed with {ptr.Info}')
            
    def DeleteFromBegin(self):
        if(self.Start is None):
            print("list is empty")
        else:
            self.Start=self.Start.Next
    def DeleteFromPosition(self,Position):
        if(self.Start is None):
            print("list is empty")
        elif(Position==1):
            self.Start=self.Start.Next        
        elif (Position > 0 and Position <= self.Count()):
            ptr=self.Start
            for i in range(1,Position -1):
                ptr=ptr.Next
            ptr.Next=ptr.Next.Next
        else:
            print("position not find")
    def sort_list(self):
        current=self.Start.Next
        while(current.Next !=None):
            ptr=self.Start
            while(ptr.Next !=None and ptr.Info<=current.Info):
                if (current.Info<ptr.Info):
                    f=current.Info
                    temp=ptr.info
                    ptr.info=current.Info
                    while(current.Info==f):
                        ptr.Info=ptr.Next.Info
                        ptr=ptr.Next
            current=current.Next

                    
                    
                
                    
                     
                        
                        


# In[ ]:



object1=linkedlist(22)  

print('1st attempt: insert at begining')          
object1.inertatBegnning(27)
object1.inertatBegnning(16)
object1.inertatBegnning(14)
object1.Print()
print("sort")
object1.sort_list()
object1.Print()


# In[ ]:





# In[ ]:




