#!/usr/bin/env python
# coding: utf-8

# In[2]:


word = input()
n = int(input())
print((word+" ")*n, end='')


# In[6]:


n = int(input())
print(n%10)


# In[16]:


number_of_days = int(input())
years = number_of_days//365
k = number_of_days%365
weeks = k//7
days = k%7
print(str(years)+" years " +str(weeks)+" weeks " +str(days)+" days")


# In[18]:


n = int(input())
m = int(input())
if n<m:
    n,m = m,n
print(n-m)


# # Python OPPs

# In[ ]:


class mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera
    def make_call(self, number):
        print("Calling....")


# In[19]:


class cart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, quantity):
        self.items[item_name]= quanity
        
    def get_cart_item(self):
        print(self.items)

cart_object = cart()
cart_object.add_tems("Books", 3)
card_object.add_tems("Laptop", 1)

cart_object.get_cart_item()


# In[ ]:




