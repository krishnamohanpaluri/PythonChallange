#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self, first_name="Sai", last_name="Megha"):
        return "{} {}".format(self.first_name, self.last_name)

person_obj = Person("Ravi", "Kumar")
full_name = person_obj.full_name()
print(full_name)


# In[2]:


class Cart:
  def __init__(self):
      self.items = {}
      self.price_details = {"book": 500, "laptop": 30000}

cart_1 = Cart()
print(cart_1.price_details)


# In[3]:


class Employee:
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name 
        self.last_name = last_name
        self.email = email
        self.pay = pay


emp_1 = Employee("Teja", "Sai", "teja.sai@company.com", 50000)
emp_2 = Employee("Sai", "Kumar", "sai.kumar@company.com", 60000)


# In[4]:


class Test:
	def __init__(self,a):
		self.a=a

	def display(self):
		print(self.a)

obj = Test()
obj.display()


# In[5]:


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        print("{} {}".format(self.first_name, self.last_name))

person_obj = Person("Ravi", "Kumar")
full_name = person_obj.full_name()
print(full_name)


# In[7]:


class Employee:
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name 
        self.last_name = last_name
        self.email = email
        self.pay = pay


emp_1 = Employee("Teja", "Sai", "teja.sai@company.com", 50000)
emp_2 = Employee("Sai", "Kumar", "sai.kumar@company.com", 60000)


# In[8]:


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self, first_name="Sai", last_name="Megha"):
        return "{} {}".format(self.first_name, self.last_name)

person_obj = Person("Ravi", "Kumar")
full_name = person_obj.full_name("Sai", "Megha")
print(full_name)


# In[ ]:


class cart:
    flat_discount = 0
    min_bill = 100
    @classmethod
    

