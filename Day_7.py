# Given an amount, write a program to find the minimum number of notes of different denominations that sum up to the given amount.
# Available note denominations are 100, 50, 10, 1.
# a = int(input())
# b = int(a/100)
# print("100:"+ str(b))
# a = a - b*(100)
# print(a)
# c = int(a/50)
# print("50:"+str(c))

# a = a - c*50
# print(a)
# d = int(a/10)
# print("10:"+str(d))
# a = a - d*10
# print("1:"+str(a))

############################################################################

# Write a program to find the minimum number of notes required for the amount M. Available note denominations are 2000, 500, 200, 50, 20, 5, 2, 1.

# a = int(input())
# b = int(a/2000)
# a = a - b*2000
# c = int(a/500)
# a = a - c*500
# d = int(a/200)
# a = a - d*200
# e = int(a/50)
# a = a - e*50
# f = int(a/20)
# a = a - f*20
# g = int(a/5)
# a = a - g*5
# h = int(a/2)
# a = a - h*2

# print("2000:"+str(b)+" "+ "500:"+str(c)+" "+"200:"+str(d)+" "+"50:"+str(e)+" "+"20:"+str(f)+" "+"5:"+str(g)+" "+"2:"+str(h)+" "+"1:"+str(a))


# Write a program to find the minimum number of notes required for the amount M. Available note denominations are 500, 50, 10, 1.

# a = int(input())
# b = int(a/500)
# a = a - b*500
# c = int(a/50)
# a = a - c*50
# d = int(a/10)
# a = a - d*10
# # print("500:"+str(b)+" "+"50:"+str(c)+" "+"10:"+str(d)+" "+"1:"+str(a))
######################################################################

# Write a program to print integers from 1 to the given integer (N).
# n = int(input())
# counter = 0
# while counter < n:
#     counter = counter+1
#     print(counter)
#############################################################################################################

# Given two integer numbers M and N, write a program to print the integers from M to N.
# m = int(input("Enter small number: "))
# n = int(input("Enter big number: "))
# counter = 0

# #if m>n:
# while counter <= (n-m):
#     print(m+counter)
#     counter = counter+1
##########################################################################################

# Write a program to print a solid square pattern of 
# N rows and N columns using the asterisk character (*), where integer N is given as an input.     
# n = int(input("Enter No of Rows: "))
# m = int(input("Enter No of Columns: "))
# counter = 0
# while counter < m:
#     counter = counter + 1
#     print("* "*n)
    
###################################################################################3

# Given an integer number (N) as input. Write a program to print the right-angled triangular pattern of N lines using an asterisk(*) character.

# n = int(input())
# counter = 1
# while counter<n:
#     print(counter*"* ")
#     counter = counter+1

#########################################################################################

# Given an integer number (N) as input. Write a program to print the sum of first N natural numbers.

# n = int(input())
# counter = 0
# total = 0
# while counter<n:
#     counter = counter + 1
#     total = total + counter
# print(total)

##########################################################################################

# n = int(input())
# counter = 0
# while counter < n:
#     m = int(input())
#     print(m)
#     counter = counter + 1

########################################################################################

#Given an integer N, write a program which reads N inputs and prints the sum of the given input integers.
# n = int(input())
# counter = 0
# total = 0
# while counter < n:
#     m = int(input())
#     counter = counter + 1
#     total = total+m
    
# print(total)
#########################################################################################

#Given an integer N. Write a program to print integers from N to 1.
# n = int(input())
# while n>0:
#     print(n)
#     n =  n - 1
####################################################################################

# n = int(input("Enter No of Rows: "))
# m = int(input("Enter No of Columns: "))
# counter = 0
# while counter < n:
#     counter = counter + 1
#     print("+ "*m)


##################################################################################33

#Given an integer N, write a program which reads N inputs and prints the product of the given input integers.

# n = int(input())
# counter = 0
# total = 1
# while counter < n:
#     m = int(input())
#     counter = counter + 1
#     total = total*m
# print(total)
##########################################################################################

# Given an integer number N as input. Write a program to print the double triangular pattern of N lines using an asterisk(*) character as shown below.
# Note: There is a space after each asterisk * character.

# n = int(input())
# m = n
# counter = 1
# while counter <= n:
#     print("* "* counter)
#     counter = counter + 1
# c = 1
# while c <= m :
#     print("* "* c)
#     c = c + 1


