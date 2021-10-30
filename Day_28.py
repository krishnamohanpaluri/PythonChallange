#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Cart:
    Flat_discount = 0
    min_bill = 100
    def _init__(self):
        self.items = {}
    
    def add_items(self, item_name, item_quantity):
        self.items[item_name] = quantity
        
    def display_items(self):
        print(self.items)

a.Cart()
a.add_item("Book", 33)
a.display_items()
print(a.items)


# Conversion of temps

# In[16]:


temp = input()
int_temp = float(temp[:-1])
if temp[-1:] == "C":
    temp_in_kelvin = int_temp + 273
    temp_in_F = (int_temp*(9/5))+32
    print(str(int_temp)+"C")
    print(str(temp_in_F)+"F")
    print(str(temp_in_kelvin)+"K")
elif temp[-1:] == "F":
    temp_in_C = (int_temp - 32)*(5/9)
    temp_in_F = (int_temp)
    temp_in_K = temp_in_C+273
    print(str(temp_in_C)+"C")
    print(str(temp_in_F)+"F")
    print(str(temp_in_K)+"K")
else:
    temp_in_C = temp_in_K - 273
    temp_in_F = (temp_in_C*(9/5))+32
    temp_in_K = int_temp
    print(str(temp_in_C)+"C")
    print(str(temp_in_F)+"F")
    print(str(temp_in_K)+"K")

    


# In[15]:


k = 'krishna'
print(k[-1:])


# In[ ]:




