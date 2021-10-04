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
















