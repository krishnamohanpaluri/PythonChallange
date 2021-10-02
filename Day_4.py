#CodigPractice_Q5:
# Write a program to print if the given number is divisible by any of the lucky numbers 6, 3, 2 in decreasing order of priority(6 is luckier than 3 and 3 is luckier than 2).
# Print "Number is divisible by" followed by the luckiest number among the above 3 which can divide the number.
# Print "Number is not divisible by 2, 3 or 6" if the number is not divisible by any of them.'
# number = int(input())

# if (number % 2 == 0) and (number % 3 ==0):
#     print("Number is divisible by 6")

# if (number % 2 != 0) and (number % 3 ==0):
#     print("Number is divisible by 3")
# if (number % 2 == 0) and (number % 3 !=0):
#     print("Number is divisible by 2")
# if (number % 2 != 0) and (number % 3 !=0) and (number % 6 !=0):
#     print("Number is not divisible by 6,3,2")
###########################################################
#CP_4 Q6: Given two positive integers, which is a number and a power. 
# Write a program to calculate the power of the given number.
# number = int (input())
# power = int (input())
# print(number**power)
############################################################

#CP_4 Q7: Given two integers a and b, write a program to find the greatest among the powers of each other.
# A  = int(input())
# B = int(input())
# if (A**B<B**A):
#     print(B**A)
# else:
#     print(A**B)
############################################################

# Given a two-digit number, print "Lucky Number" if any of the following conditions are satisfied
# 	1. The number is a multiple of 9
# 	2. One of the digits is 9
# Print "Unlucky Number" in all other cases.
# number = int(input())
# a = int(number/10)
# b = number % 10 
# print(a, b)
# if (number == 0) or (a == 9 or b == 9):
#     print("Lucky Number")
# else:
#     print("Unlucky Number") 
############################################################
