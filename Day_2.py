#Q_1: Write a program to convert the given integer to a positive integer
#integer = int(input("Enter your Integer: "))
#if integer<0:
#    print(integer*(-1))
#else:
#    print(integer)
############Conditional Statments#######################
#Q_2 Write a program to print "positive" if the input is positive and negative
Number = int(input("Enter your Number: "))
if Number>0:
#Number = int(input("Enter your Number: "))
#if Number>0:
#    print(str(Number)+" is a positive Number")
#else:
#    print(str(Number)+" is a negative number")

###################################################################################

#CodingPractice_Q1:  You're given a word and an index position of a character. You need to write 
# a program that prints the given word without the character at the given index.
#string_1 = input("Enter your string: ")
#char_position = int(input("Enter the charecter position: "))
#print(string_1[char_position])
#print(string_1[:char_position])
#string_2 = string_1[:char_position] + string_1[(char_position+1):] 
#print(string_2)
######################################################################

#CodingPractice_Q2: Write a program to check if the given string is a valid password or not. 
#A string is considered as a valid password if the number of characters present is greater than 7.
#password = input("Enter your Password: ")
#if len(password) >= 7:
#   print(True)
#else:
#    print(False)
##############################################################
# CodingPractice_Q4: Write a program which checks whether the given number N is between 25 and 75.

#number = int(input("Enter your number: "))
#if (number < 25) or (number > 75):
#    print(False)
#else:
#    print(True)

#############################################################
#CodingPractice_Q5: Write a program that reads a single line of input and prints the first and last characters of the given 
# input and prints the asterisk character (*) in place of the remaining characters.
#CodingPractice_Q6: Write a program that reads a single line of input and prints the first two and last two characters of the given input and prints the asterisk character (*) in place of the remaining characters.
#string_1 = input("Enter your string: ")
#string_2 = string_1[:2]+ "*"*(len(string_1)-4) +string_1[-2:]
#print(string_2)
################################################################

###################Assignment-2#################################
#CodingPractice_A2: Given a student has scored M marks in Maths, P marks in Physics and C marks in Chemistry. Write a program to check if a student is eligible for admission in a professional course. If any one of the below conditions is satisfied, then the student is eligible.
#1) M >= 70 and P >= 60 and C >= 60
#2) M + P + C >= 180

#M = int(input("Enter Maths Marks: "))
#P = int(input("Enter Physics Marks: "))
#C = int(input("Enter Chemistry Marks: "))
#if ((M >=70) and (P>=60) and (C>=60)) or (M+P+C>=180):
#    print(True)
#else:
#    print(False)

#####################################################################
#Coding Practice_3
####################################################################

#Q1: Write a program to print the greatest among the two numbers.
#number_1 = int(input())
#number_2 = int(input())
#if number_1>number_2:
#    print(number_1)
#else:
#    print(number_2)

#Q2: Write a program to check if the given two numbers are equal.
#number_1 = int(input())
#number_2 = int(input())
#if number_1 == number_2:
#    print("Equal")
#else:
#    print("Not Equal")

#Q3: Write a program to find if the given number is positive, negative, or zero.
#number = int(input())
#if number>0:
#    print("Positive")
#if number<0:
#    print("Negative")
#if number == 0:
#    print("Zero")

#Q4: A person is eligible to vote if his/her age is at least 18 years. Write a program 
# that checks if a person is eligible to vote based on the person's age.
#age = int(input())
#if age<18:
#    print("Not Eligible")
#if age >=18:
#    print("Eligible")

#Q5: Given the length and breadth of a box, check if it is a Rectangle or Square.
#length = int(input())
#breadth = int(input())
#if length == breadth:
#    print("Square")
#else:
#    print("Rectangle")

#Q6: A company decided to give a bonus of 5% to an employee if his/her years of service is more than five years.
    #Write a program that reads an employee's salary and years of service and decides whether the employee gets the bonus or not.
#salary = int(input())
#experience = int(input())
#if experience>5:
#    print(salary*(5/100))
#else:
#    print("No Bonus")


#Q7: Given three angles of a triangle, write a program to check whether the triangle is valid or not. A triangle is valid if the 
# sum of its three angles is equal to 180 degrees.
#a = int(input())
#b = int(input())
#c = int(input())
#if a+b+c>180:
#    print("It's not a Triangle")
#else:
#    print("It's a Triangle")

#Q8: Given the lengths of three sides of a triangle, write a program to check whether the triangle is valid or not.
        #For a triangle to be valid, the sum of lengths of any two sides of the triangle must be greater than the third side. 
a = int(input())
b = int(input())
c = int(input())

if (a+b>c) or (b+c>a) or (c+a>b):
    print("It's a Triangle")
else:
    print("It's not a Triangle")









