# Given day number D as input, write a program to display the day name. 
# (1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday)
# D = int(input())

# if D == 1:
#     print("Monday")
# elif D == 2:
#     print("Tuesday")
# elif D == 3:
#     print("Wednesday")
# elif D == 4:
#     print("Thursday")
# elif D == 5:
#     print("Friday")
# elif D == 6:
#     print("Saturday")
# else:
#     print("Sunday")
#####################################################################

#Write a program to print the relation between two numbers, A and B

# A = int(input())
# B = int(input())
# if A == B:
#     print("A == B")
# elif A > B:
#     print("A > B")
# elif A < B:
#     print("A < B")

######################################################################

# The amount at which a product is sold by the seller is known as the Selling Price. The amount at which the seller has acquired the product is known as the Cost Price.
# If the Selling Price of a product is higher than its cost price, then the seller has made a profit. If it is lesser, then the seller has incurred loss selling that product. If the Selling Price is equal to the Cost Price, it means the seller has made No Profit and No loss, by selling the product.
# Given Cost price CP and selling price SP of a product, write a program to determine whether the seller made a profit, incurred loss, or made no profit or loss. 
# CP = int(input())
# SP = int(input())
# if SP<CP:
#     print("Loss")
# elif SP>CP:
#     print("Profit")
# else:
#     print("No Profit -  No Loss")
##########################################################################

# Write a program to determine whether the given year Y is a leap year or not.
# A normal year consists of 365 days. But the time required for Earth to revolve around the Sun is around 365.2425 days. So a "leap year" of 366 days is used once every four years to eliminate the error caused by three normal (but short) years. Any year that is divisible by 4 is usually a leap year: for example, 1988, 1992, and 1996 are leap years. 
# However, there is still a small error that must be accounted for. To eliminate this error, the calendar considers that a year that is divisible by 100 (for example, 1900) is a leap year only if it is also divisible by 400. For this reason, the following years are not leap years: 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600, ...
# This is because they are divisible by 100 but not by 400.
# The following years are leap years: 1600, 2000, 2400
# This is because they are divisible by both 100 and 400.
# year = int(input())
# if year%4 == 0:
#     print(False)
# elif  year%4 == 0 and year%100 == 0 and year%400 ==0:
#     print(False)
# else:
#     print(False)
############################################################################################

#Write a program to display a customized message based on temperature T
# temp = float(input())
# if temp <0:
#     print("Freezing weather")
# elif temp>=0 and temp<10:
#     print("Very Cold weather")
# elif temp >=10 and temp<20:
#     print("Cold weather")
# elif temp >=20 and temp<30:
#     print("Normal")
# elif temp >=30 and temp<40:
#     print("Hot")
# else:
#     print("Very Hot")

#########################################################################
# It was Raj's first day at school. His teacher Anu asked the students to meet every other student in the class and to introduce themselves. The teacher asked them to do handshakes when they meet each other.
# If there are N number of students in the class then write a program to print the total number of handshakes made by the students.
# n = int(input())
# print(int(n*((n+1)/2))-n)

########################################################################

# The possible denominations of currency notes are 100, 50, 20 and 10. The amount A to be withdrawn is given as input.
# Write a program to break the amount into minimum number of bank notes.
# N = int(input())
# a = int(N/100)
# k = a*100
#     #print(str(a)+ "*" + str(100))
# print("100 Notes: "+str(a))
# N = N - k
#     #print(a)
#     #print(N)
# b = int(N/50)
# l = b*50
#     #print(str(b)+"*"+str(50))
# print("50 Notes: "+str(b))
# N = N-l
#     #print(N)
# c = int(N/20)
# m = c*20
#     #print(str(c)+"*"+str(20))
# print("20 Notes: "+str(c))
# N = N-m
# d = int(N/10)
# n = d*10
# #     #print(str(d)+"*"+str(10))
# # print("10 Notes: "+str(d))

# ###################################################################

# # Write a program to find the minimum number of notes required for the amount M. 
# # Available note denominations are 2000, 500, 200, 50, 20, 5, 2, 1.

# N = int(input())
# a = int(N/2000)
# k = a*2000
# print(str(a)+ "*" + str(2000))
# #print("100 Notes: "+str(a))
# N = N - k
#      #print(a)
#      #print(N)
# b = int(N/500)
# l = b*500
# print(str(b)+"*"+str(500))
# #print("50 Notes: "+str(b))
# N = N-l
#      #print(N)
# c = int(N/200)
# m = c*200
# print(str(c)+"*"+str(200))
# #print("20 Notes: "+str(c))
# N = N-m
# d = int(N/50)
# n = d*50
# print(str(d)+"*"+str(50))
# #print("10 Notes: "+str(d))

day_0 = input("Enter the day: ")
day_n = int(input("Enter the number of day: "))
day_1 = "Monday"
day_2 = "Tuesday"
day_3 = "Wednesday"
day_4 = "Thursday"
day_5 = "Friday"
day_6 = "Saturday"
day_7 = "Sunday"

if day_0 == "Monday":
    if day_n%7 == 1:
        print(day_1)
    elif day_n%7 == 2:
        print(day_2)
    elif day_n%7 == 3:
        print(day_3)
    elif day_n%7 == 4:
        print(day_4)
    elif day_n%7 == 5:
        print(day_5)
    elif day_n%7 == 6:
        print(day_6)
    elif day_n%7 == 0:
        print(day_7)

elif day_0 == "Tuesday":
    if day_n%7 == 1:
        print(day_2)
    elif day_n%7 == 2:
        print(day_3)
    elif day_n%7 == 3:
        print(day_4)
    elif day_n%7 == 4:
        print(day_5)
    elif day_n%7 == 5:
        print(day_6)
    elif day_n%7 == 6:
        print(day_7)
    elif day_n%7 == 0:
        print(day_1)

elif day_0 == "Wednesday":
    if day_n%7 == 1:
        print(day_3)
    elif day_n%7 == 2:
        print(day_4)
    elif day_n%7 == 3:
        print(day_5)
    elif day_n%7 == 4:
        print(day_6)
    elif day_n%7 == 5:
        print(day_7)
    elif day_n%7 == 6:
        print(day_1)
    elif day_n%7 == 0:
        print(day_2)

elif day_0 == "Thursday":
    if day_n%7 == 1:
        print(day_4)
    elif day_n%7 == 2:
        print(day_5)
    elif day_n%7 == 3:
        print(day_6)
    elif day_n%7 == 4:
        print(day_7)
    elif day_n%7 == 5:
        print(day_1)
    elif day_n%7 == 6:
        print(day_2)
    elif day_n%7 == 0:
        print(day_3)

elif day_0 == "Friday":
    if day_n%7 == 1:
        print(day_5)
    elif day_n%7 == 2:
        print(day_6)
    elif day_n%7 == 3:
        print(day_7)
    elif day_n%7 == 4:
        print(day_1)
    elif day_n%7 == 5:
        print(day_2)
    elif day_n%7 == 6:
        print(day_3)
    elif day_n%7 == 0:
        print(day_4)

elif day_0 == "Saturday":
    if day_n%7 == 1:
        print(day_6)
    elif day_n%7 == 2:
        print(day_7)
    elif day_n%7 == 3:
        print(day_1)
    elif day_n%7 == 4:
        print(day_2)
    elif day_n%7 == 5:
        print(day_3)
    elif day_n%7 == 6:
        print(day_4)
    elif day_n%7 == 0:
        print(day_5)

elif day_0 == "Sunday":
    if day_n%7 == 1:
        print(day_7)
    elif day_n%7 == 2:
        print(day_1)
    elif day_n%7 == 3:
        print(day_2)
    elif day_n%7 == 4:
        print(day_3)
    elif day_n%7 == 5:
        print(day_4)
    elif day_n%7 == 6:
        print(day_5)
    elif day_n%7 == 0:
        print(day_6)


 








