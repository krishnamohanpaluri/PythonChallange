################################################
# units = int(input("enter no of Units: "))
# if units<=50:
#     first50 = units*2
#     print(first50+(0.2*first50))
# elif units>50 and units<=150:
#     units = (units - 50)
#     second100 = (units)*3
#     print(100+second100+(0.2*(100+second100)))
# elif units>150 and units<=250:
#     units = units-150
#     third150 = units*5
#     print(100+300 +third150+(0.2*(400+third150)))
# elif units>250:
#     units =  units - 250
#     lastunits = units*8
#     print(650+lastunits + (0.2*(650+lastunits)))

##################################################
#cp10_p3
# string = input()
# string = string.lower()
# reverse_string = string[::-1]
# reverse_string = reverse_string.lower()

# if string == string[::-1] :
#    print("Palindrome")
# else:
#     print("Not a Palindrome")

##################################################
#cp10_p4
# no_of_inputs = int(input())
# first_number = int(input())
# greatest_number = first_number
# for i in range(no_of_inputs-1):
#     number = int(input()) 
#     if number>greatest_number:
#     #if number<greatest_number: #cp10_p5
#         greatest_number = number
# print(greatest_number)

##################################################

#cp10_p6:
# number = int(input())
# total = 0
# seriesTotal=0
# for i in range(0, number):  
#     j = (10**i)*2
#     total = total + j
#     seriesTotal = seriesTotal+total
# print(seriesTotal)

#####################################################

#cp10_p7&8:
# number = int(input())
# total = 0
# for i in range(1, number+1):
#     if (number%i == 0):
#         #print(i)
#         total = total+i
# print(total)
###############################################

#cp10_p9
# n = int(input())
# total = 0
# for i in range(1, n):
#     if (n % i == 0):
#         total = total + i
# if total == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")

###############################################

#cp10_p10
# n = int(input())
# n = str(n)
# total = 0
# for i in n:
#     i = int(i)
#     j =(i**(len(n)))
#     total = total + j
# if total == int(n):
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

















