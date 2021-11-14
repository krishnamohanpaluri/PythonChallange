#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[16]:


alphabet = {' ':' ','a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26','A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':'13', 'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26'}
string = input()
string1 =''
for k in string:
    for i,j in alphabet.items():
        if k == i:
            string1+=("-"+j)
print(string1[1:-1])
            


# In[15]:


string = input().split(" ")
print(string)


# In[9]:


string = input().split(" ")
for i in string:
    


# In[11]:


k = "Krishna"
print(k[1:-1])


# In[17]:





# In[18]:


L=int(input("Enter a limit: "))
count=0
for a in range(1,L-1):
    for b in range(a+1,L):
         for c in range(b+1,L+1):
                x=a*a
                y=b*b
                z=c*c
                if (x+y==z):
                     count+=1


print(count)


# In[19]:


n = int(input('Enter your number here: '))
list1 = []
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i **2 +j**2 == k**2:
                list1.append([i,j,k])
                list2 = [sorted(x) for x in list1]
                set1 = [tuple(x) for x in list2]
                set2 = set(set1)
                set3 = [list(j) for j in set2]
                len(set3)


# In[20]:


n = int(input('Enter your number here: '))
list1 = []
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i **2 +j**2 == k**2:
                list1.append([i,j,k])
                list2 = [sorted(x) for x in list1]
                set1 = [tuple(x) for x in list2]
                set2 = set(set1)
                set3 = [list(j) for j in set2]
len(set3)


# In[27]:


#m = int(input())
n = int(input())
list1 = []
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i**2 + j**2 == k**2:
                list1.append([i,j,k])
                list2 = [sorted(x) for x in list1]
                set1 = [tuple(x) for x in list2]
                set2 = set(set1)
                set3 = [list(j) for j in set2]
print(len(set3))


# In[29]:


N=int(input())
K=int(input())
counter=N-1
for i in range(K):
    for j in range(i+1):
        counter+=1
for i in range(K):
    for j in range(i+1):
        print(counter,end=" ")
        counter-=1
    print()


# In[33]:


A=int(input())
B=int(input())


for i in range(A, B+1):
    x = len(str(i))
    sum1 = 0
temp = i
while temp > 0:
    digit = temp % 10
    sum1 += digit ** x
    temp //= 10
    if i == sum1:
        print(i)


# In[36]:


b = int(input())
is_any_armstrong = False # initialise it with False
for num in range(a,b+1):
    ...
    if num == sum:
        is_any_armstrong = True # we got an armstrong number, so set it to True
        print(num,end= " ")
if is_any_armstrong == False: # if there is no armstrong number
    print("-1")


# In[39]:


a = str(input())
b = str(input())
answer = ""
len1, len2 = len(a), len(b)
for i in range(len1):
    match = ""
    for j in range(len2):
        if (i + j < len1 and a[i + j] == b[j]):
            match += b[j]
        else:
            if (len(match) > len(answer)):
                answer = match
                match = ""
print(answer)


# In[4]:


students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
string = input().split(" ")
for i in range(len(string)):
    students_dict[string[i]] = (string[(i+1)])
print(students_dict)


# In[5]:


m = int(input())
n = int(input())
lst = [0, 0] + [1] * (n - 1)

for i in range(int(n ** 0.5 +1)):
# print('i:', i)
    if lst[i]:
        for j in range(2, n // i + 1):
# print('j:', j)
        lst[j * i] = 0
            for i in range(m, n + 1):
if not lst[i]:
    print(i)


# In[ ]:




