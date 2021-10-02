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
# ############################################################
# Assignment-4: 
#Q1: Write a program to print the triple of number N if it is a
#  multiple of 3 otherwise, double of N.
# N = int(input())
# if (N%3==0):
#     print(N*3)
# else:
#     print(N*2)
################################################################

#Q2: You are given two integers, a and b. Print the smallest value among a%b and b%a.
# a = int(input())
# b = int(input())
# if (a%b < b%a):
#     print(a%b)
# else:
#     print(b%a)
#################################################################

#Q3: Given a number N, find whether the number is common or uncommon. A number is considered uncommon 
# if it is not divisible by any of the single-digit primes.
# N = int(input())
# if (N%2 !=0) and (N%3 !=0) and (N%5 !=0) and (N%7 !=0):
#     print(True)
# else:
#     print(False)
###############################################################

#Q4:
# Write a program to find the hypotenuse H of a right-angled triangle of sides A and B.
# Note: Pythagoras theorem states that, for a right-angled triangle. Hypotenuse2 = A2 + B2
# A = int(input())
# B = int(input())
# C = int(((A**2)+(B**2))**(0.5))
# print(C)
#################################################################

#Q5: 
# Write a program to check if a given 3-digit number X is an Armstrong number or not.
# Note: A number is an Armstrong number if the number is equal to the sum of the Nth power of its digits.
# X = input()
# Y = len(X)
# #print(X)
# #print(Y)
# X = int(X)
# first_digit = int(X/100) #first digit
# b = int(X%100)
# second_digit = int(b/10) #second digit
# third_digit = int(b%10) #third digit
# print(first_digit)
# print(second_digit)
# print(third_digit)

# if((first_digit**Y)+(second_digit**Y)+(third_digit**Y) == X):
#     print(True)
# else:
#     print(False)
###############################################################

#Q6: Given two integers, they are considered a lucky pair 
# if any one of them is 6 or if their sum or difference is equal to 6.
# number_1 = int(input())
# number_2 = int(input())
# if (number_1 == 6 or number_2 == 6) or (number_1 + number_2 == 6 or number_1 - number_2 == 6):
#     print("Lucky")
# else:
#     print("Unlucky")

######################################################################
#Q7: Write a program which prints the greatest among the given three numbers.
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())

# if (number_1 > number_2 and number_1 > number_3):
#     print(number_1)
# if (number_2 > number_3 and number_2 > number_1):
#     print(number_2)
# if (number_3 > number_1 and number_3 > number_2):
#     print(number_3)
# if (number_1 == number_2 == number_3):
#    print(number_3)
#####################################################################
#               Coding Practice 5
#Q1: Given two integers A and B, write a program to print the relation between the two numbers.
# A = int(input())
# B = int(input())
# if A == B:
#     print("A=B")
# elif A>B:
#     print("A>B")
# elif A<B:
#     print("A<B")
########################################################################

#Q2: Write a program to calculate the grade of the student based on marks he/she scored.
# marks = float(input())
# if marks>=85:
#     print("A")
# elif marks>70 and marks<=80:
#     print("B")
# elif marks>=60 and marks<=70:
#     print("C")
# else:
#     print("F")

##########################################################################
#Q3: Write a program to print a greeting message based on the given time.
# time = float(input())
# morning = time>=4 and time<12
# afternoon = time>=12 and time <16
# evening = time>=16 and time<20
# night = time>=20 and time<4

# if morning:
#     print("Good Morning")
# elif afternoon:
#     print("Good Afternoon")
# elif evening:
#     print("Good Evening")
# else:
#     print("Good Night")
##########################################################################

#Q4: Given the number of sides, write a program to print the name of the polygon.
# no_of_sides = int(input())
# if no_of_sides <=5:
#     if no_of_sides == 5:
#         print("Pentagon")
#     elif no_of_sides == 4:
#         print("Quadrilateral")
#     elif no_of_sides == 3:
#         print("Triangle")
#     elif no_of_sides<=2:
#         print("Not Polygon")
# else:
#     print("Big Polygon")    

















