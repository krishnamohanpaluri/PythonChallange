#!/usr/bin/env python
# coding: utf-8

# # Fuctions Excersize.

# 1. Write a Program to print the largets of three numbers.

# In[2]:


def max_of_two(x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))
a = int(input())
b = int(input())
c = int(input())
max_of_three(a,b,c)


# 2. write a program multiply all the numbers in a given list/tuple/set

# In[6]:


def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
n = int(input())
numbers=[]
for i in range(n):
    k = int(input())
    numbers.append(k)

multiply(numbers)


# In[27]:


n = int(input())
for i in range(1, n+1):
    spaces = " "*(i-1)
    k = n - (i-1)
    number = ''
    for j in range(1,k+1):
            number = number + (str(j)+' ')
    print(spaces+number)
      


# In[25]:


n = int(input())
for row in range(1, n+1):
    left_spaces = " " * (row-1)
    i = n - (row-1)
    numbers = ""
    for j in range(1, i+1):
        numbers = numbers + (str(j) + " ")
    print(left_spaces + numbers)


# In[38]:


n = int(input())
print("* "*n)
for i in range(1, n-1):
    stars = "* "
    space ="  "*((n - i-2))
    patern = stars+space+stars 
    print(patern)
print("* ")


# In[29]:


N = int(input())

print("* ")
for i in range(N-2):
    hollow_spaces = " "*(2*i)
    hollow_line = "* " + hollow_spaces + "* " 
    print(hollow_line)

star_line = "* " * N
print(star_line)


# In[35]:


N = int(input())

star_line = "* " * N
print(star_line)

for row in range(1, N-1):
    hollow_spaces = "  "*(N-row-2)
    hollow_line = "* " + hollow_spaces + "* "
    print(hollow_line)

print("* ")


# In[ ]:




