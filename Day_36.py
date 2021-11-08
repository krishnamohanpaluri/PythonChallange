#!/usr/bin/env python
# coding: utf-8

# In[5]:


def digits(N):
    st = ""
    for i in range(1, N+1):
        st += str(i)
    print(len(st))
N = int(input())
digits(N)


# In[6]:


number1 = int(input())
number2 = int (input())
count = 0
for i in range(number1, number2+1):
        if int(i**0.5)== i**0.5:
            count = count + 1
print(count)


# In[36]:


n = int(input())
print("* "*(n))
for i in range(1,n):
    #space1 = "  "*i
    space2 = " "*(n-1)
    star = "* "
    #star2 = "*"+(" "*(n-1))
    total = star+space2+star
    print(total)


# In[44]:


n = int(input())
print("* "*(n))
for i in range(1,n):
    space1 = " "*(n-1)
    star = " *"
    space2 = " "*(i)
    total = space2+star+space1+star
    print(total)


# In[47]:


n = int(input())
for i in range(1, n):
    spaces = "  "*(n-i)
    star = "*"
    total = spaces+star
    print(total)
    


# In[51]:


n = int(input())
for i in range(n):
    print("  "*(n-i)+"* "*i)


# In[65]:


n =int(input())
for i in range(n):
    space = "  "*i
    star = " *"*(n-i)
    print(space+star)


# In[80]:


n = int(input())
x = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    if i%2 == 0:
        even_sum += (x**i)
print(even_sum)
print()
for j in range(1, n+1):
    if j%2 == 1:
        odd_sum += (x**j)
print(odd_sum)
total = even_sum - odd_sum
print(total)


# In[99]:


x = int(input())
n_terms = int(input())
y = 2*n_terms
empty_list = []
for i in range(y):
    if i%2 == 1:
        empty_list.append(x**(i))
#print(empty_list)
even_sum = 0
odd_sum = 0
for i in range(len(empty_list)):
    if i%2 == 0:
        #print(empty_list[i])
        even_sum+=empty_list[i]
#print(even_sum)
for j in range(len(empty_list)):
    if j%2 == 1:
        #print(empty_list[i])
        odd_sum+=empty_list[j]
#print(odd_sum)
print(even_sum-odd_sum)


# In[ ]:





# In[ ]:


k = [1,3,4,5,6,7,8,0]
for i in k:
    

