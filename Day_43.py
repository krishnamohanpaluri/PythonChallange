#!/usr/bin/env python
# coding: utf-8

# In[38]:


n = int(input())
m = int(input())
list_1 = []
if n>m:
    n,m = m,n
for i in range(n, m+1):
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                list_1.append(i)
a = set(list_1)
b = list(a)
b = sorted(b)
for i in b:
    print(i)


# In[ ]:





# In[35]:


lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            print(num)


# In[17]:


n = int(input())
a = int(n/1000)
b = n - a*1000
c = int(b/500)
d = b - c*500
e = int(d/100)
f = d - e*100
g = int(f/50)
h = f - g*50
i = int(h/20)
j = h - i*20
k = int(j/5)
l = j - k*5
print("1000:"+str(a))
print("500:"+str(c))
print("100:"+str(e))
print("50:"+str(g))
print("20:"+str(i))
print("5:"+str(k))
print("1:"+str(l))


# In[6]:



ab = str(input()).lower()
an = str(input()).lower()
if ab == an: #both equals its a tie
    print("Tie")
elif ab == "rock" and an == "sissors": #Rock wins
    print("Abhinav Wins")
elif ab == " sissors" and an == "paper": #sissors wins
    print("Abhinav Wins")
elif ab == "paper" and an == "rock": #Paper wins
    print("Abhinav Wins")
    
elif an == "rock" and ab == "sissors": #Rock wins
    print("Anjali Wins")
elif an == " sissors" and ab == "paper": #sissors wins
    print("Anjali Wins")
elif an == "paper" and ab == "rock": #Paper wins
    print("Anjali Wins")
    


# In[1]:


abhinav = str(input("Abhinav's choice:"))
anjali = str(input("Anjali's choice:"))
if not ((anjali.lower() in ["rock", "paper", "scissors"]) and (abhinav.lower() in ["rock", "paper", "scissors"])):
    print("Invalid input")#Checking the correctness of the input
else:
    if abhinav.lower() == anjali.lower():#If both players made the same choice, then a draw
        print("Draw")
    elif abhinav.lower() == "rock":
if anjali.lower() == "paper":
    print("Anjali wins")
else:
    print("Abhinav wins")#If the first player chooses a rock, then he will lose to paper and win against the scissors
elif abhinav.lower() == "paper":
    if anjali.lower() == "rock":
        print("Abhinav wins")
    else:
        print("Anjali wins")#If the first player chose paper, then he will lose with scissors and win against a rock
    elif abhinav.lower() == "scissors":
        if anjali.lower() == "rock":
            print("Anjali wins")
        else:
            print("Abhinav wins")#If the first player chooses scissors, then he will lose to the rock, he will win against the paper


# In[2]:


a = str(input()).lower()
print(a)


# In[47]:


a = int(input())
b = int(input())
armstrong_numbers = []
for i in range(a, b+1):
    i = str(i)
    l = len(i)
    sum = 0
    for char in i:
        char = (int(char))**l
        print(char)


# In[45]:


a = int(input())
#print(len(a))
a = str(a)
print(len(a))


# In[49]:


n = int(input())
n_list = []
for i in range(1, n+1):
    k = int(input())
    n_list.append(k)
for i in n_list:
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count+=1
    if count < 0:
        print(i)


# In[53]:


n = int(input("Enter a positive integer: "))


is_primes = [] # list of potential prime numbers(contains primes and non primes)


for count in range(n):
    read = int(input("> "))
    is_primes.append(read)


non_primes = []

for num in is_primes:
    if num == 2 or num == 3:
        pass
    else:
        for i in range(2, num):
            if num % i == 0:
                non_primes.append(num)
                break
            else:
                pass
print(is_primes - non_primes)



# In[63]:


temp = input()
T = float(temp[:-1])
print(temp)
print(int_temp)
if temp[-1:] == "C":
    print(T)


# In[ ]:




