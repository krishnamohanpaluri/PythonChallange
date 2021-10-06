#Write a program to print integers from 1 to the given integer (N).
#Note: Use For Loop

# n = int(input())
# for i in range(1 , n+1):
#     print(i)
############################################################################################################

# Given two integer numbers M and N, write a program to print the integers from M to N.
# Note: Use For Loop

# m = int(input())
# n = int(input())
# for i in range(m, n+1):
#     print(i)

############################################################################################################

# Write a program to print a solid square pattern of N rows and N columns using the asterisk character (*), where integer N is given as an input.
# Note: Use For Loop
# n = int(input())
# for i in range(n):
#     print("* "*n)

############################################################################################################

#Given two integers M and N, write a program to print a solid rectangle pattern of M rows and N columns using the asterisk character (*).
#Note: Use For Loop
n = int(input())
m = int(input())

for i in range(n,m):
    print(i*"* ")


