#Coding Practice_Q5: Write a program to find season for the given month number.
# month = int(input())
# if (month == 11 or month ==12 or month == 1):
#     print("Winter")
# elif (month == 2 or month == 3):
#     print("Spring")
# elif (month == 4 or month ==5 or month == 6):
#     print("Summer")
# elif (month == 6 or month == 7):
#     print("Rainy")
# else:
#     print("Autumn")

###########################################################################
# Q6: Given a student's percentage of attendance and status of having a medical report. 
# Write a program to decide if a student is eligible to take the final exam.
# A = input()
# M = input()
# B = len(A)
# A = A[:(B-1)]
# A = int(A)

# if A>=75:
#     print("Allowed to write the exam")
# elif A<75 and M == "Y":
#     print("Allowed to write the exam")
# else:
#     print("Cannot write the exam")
###############################################################################

#Q7:  In this problem, you need to write a program to calculate the electricity bill for a household, based on the units of electricity the household consumed. The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned below:
# For the first 50 units (0-50), the charge is 2/unit
# For the next 100 units (51-150), the charge is 3/unit
# For the next 100 units (151-250), the charge is 5/unit
# For above 250 units (251 and above), the charge is 8/unit
# Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill



#Given an integer between 0 and 10000, write a program to print the sum of its digits.
# number = int(input())
# a = int(number /1000)
# b = int(number%1000)
# c = int(b/100)
# d = int(b%100)
# e = int(d/10)
# f = int(d%10)
# print(a+c+e+f)

#Write a program to create a menu driven calculator that performs basic arithmetic operations (+, -, *, /, and %).
# a = int(input())
# b = int(input())
# operator = input()
# if operator == "+":
#     print(a+b)
# elif operator == "*":
#     print(a*b)
# elif operator == "-":
#     print(a-b)
# elif operator == "/":
#     print(a/b)
# elif operator == "%":
#     print(a%b)

#################################################################
#Given an amount, write a program to find the minimum number of notes of different denominations that sum up to the given amount.
#Available note denominations are 100, 50, 10, 1.
##############################################################3
# While loops##############

n = int(input())


counter = 0 
while counter<n: 
    row = "* "*n
    print(row)
    counter = counter+1






















