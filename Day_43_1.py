#!/usr/bin/env python
# coding: utf-8

# In[10]:


temp = input()
T = float(temp[:-1])
char = temp[-1:]
if char == "C":
    temp_in_C = T
    temp_in_K = temp_in_C+273
    temp_in_F = round((temp_in_C*(9/5))+32, 2)
    
    print(str(temp_in_C)+"C")
    print(str(temp_in_F)+"F")
    print(str(temp_in_K)+"K")
elif char =="F":
    temp_in_F = T
    temp_in_C = round((temp_in_F - 32)*(5/9),2)
    temp_in_K = temp_in_C + 273
    
    print(str(temp_in_C)+"C")
    print(str(temp_in_F)+"F")
    print(str(temp_in_K)+"K")

elif char =="K":
    temp_in_K = T
    temp_in_C = temp_in_K - 273
    temp_in_F = round((temp_in_C*(9/5))+32,2)
    
    
    print(str(temp_in_C)+"C")
    print(str(temp_in_F)+"F")
    print(str(temp_in_K)+"K")
#print(temp, T, symbol)


# In[ ]:




