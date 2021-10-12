# # #######################################################
# #                     #Assignment10\
# # #import math
# # # n = int(input())
# # # m = int(input())
# # # count = 0
# # # for i in range(n, m+1):
# # #             k = math.sqrt(i)
# # #             if k == 
# # #                                             #     #perfect_square = i**2
# # #                                             #     square_root = i**(1/2)  
# # #                                             #     print(int(square_root%10))
# # #                                             #    # if int(square_root) == int(perfect_square):
# # #                                                 #   count = count + 1
# # #      
# # #                                       #print(count)
# # # number1 = int(input())
# # # number2 = int (input())
# # # count = 0
# # # for i in range(number1, number2+1):
# # #         root = i**2
# # #         if int(root + 0.5) == i:
# # #             count = count + 1
# # # print(count)

# # ######################Assignment10#####################
# # for row in range(6):
# #     for col in range(7):
# #         if (row == 0 and col%3!=0) or (row == 1 and col%3 == 0) or (row-col == 2) or(row+col == 8):
# #             print("* ", end="")
# #         else:
# #             print(" ", end="")
# #     print()





# #######################################################
# n = int(input("Enter your number: "))
# factors = 0
# for number in range(2, n-1):
#     for i in range(2, number-1):
#         if number%i == 0:
#             factors = factors + 1
#     if factors == 0:
#         print(number)


#####################################################


#Numbers in regular patterns

# rows = int(input())
# col = int(input())
# for i in range(1, rows+1):
#         print((str(i)+" ")*col)


##################################################
#printing dimond patterns

# rows = int(input())
# for i in range(1, rows+1):
#     print((" "*(rows-i))+"* "*i)
# for i in range(1, rows+1):    
#     print((" "*(i))+"* "*(rows-i))

#################################################
# n = int(input())

# k = n
# for i in range(1, n+1):
#     spaces = " " * k
#     stars = "* " * i
#     print(spaces+stars)
#     k = k - 1


###############################################
# rows = int(input())
# col = int(input())
# for i in range(1, rows+1):
#     if i%2==0:
#         print("- "* col)
#     if i%2==1:
#         print("+ "* col)
###############################################

rows = int(input())
col = int(input())
print("+ " + "-"*str(rows-2) +" +")
for i in range(1, rows):
    print("|"+" "*(rows - col)+"|")