###################DAY_3############################

#CodingPractice_4: Q1: Write a program to check if the given number is even or odd.
# number = int(input())
# if number%2 == 0:
#     print("Even")
# else:
#     print("Odd")
######################################################
#Q2: Write a program to read a single line of input, which is a two-digit integer and
# Print "Special Number" if any one of the following conditions are satisfied
# 	1. The sum of digits is 7
# 	2. One of the digits is 7
# 	3. The number is a multiple of 7
# Print "Normal Number" in all other cases
# number = int(input())
# a = int(number/10)
# print(a)
# b = number%10
# print(b)

# if (a+b==7) or ( a == 7 or b == 7) or (number%7==0):
#     print("Special Number")
# else:
#     print("Normal Number")

#########################################################
#Q3: A number is called Special Eleven, if it is a multiple of 11 or if it is one more than a 
# multiple of 11. 
# Write a program to check if the given number is a Special Eleven number.
# number = int(input())
# if (number%11 ==0) or (number%11==1):
#     print("Special Eleven")
# else:
#     print("Normal Number")
##########################################################
#Q4: Write a program to print if the given number is divisible by any of the lucky numbers 6, 3, 2 in decreasing order of priority(6 is luckier than 3 and 3 is luckier than 2).
# Print "Number is divisible by" followed by the luckiest number among the above 3 which can divide the number.
# Print "Number is not divisible by 2, 3 or 6" if the number is not divisible by any of them.
number = int(input())
if (number % 6 == 0) and (number % 3 == 0) and (number % 2 == 0):
    print("Number is divisible by 6")
if 3 != 0:
    pass
else:
    print("Number is divisible by 3")
if number % 2 == 0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 6, 3 or 2")
