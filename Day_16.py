# #Coding Practice 17 #Problem1
# size_of_diamond = int(input())
# #furst_row
# hollow_spaces_count = -1
# first_row = (" "*(size_of_diamond-1)+"*")
# print(first_row)
# for row in range(2, size_of_diamond+1):
#     left_spaces_count = size_of_diamond - row
#     left_spaces = left_spaces_count*" "
#     hollow_spaces_count = hollow_spaces_count+2
#     hollow_spaces = " "* hollow_spaces_count
#     row_output = left_spaces+ "*" + hollow_spaces + "*"
#     print(row_output)

# for row in range(1, size_of_diamond-1):
#     left_spaces_count = row
#     left_spaces = left_spaces_count*" "
#     hollow_spaces_count = hollow_spaces_count-2
#     hollow_spaces = " "* hollow_spaces_count
#     row_output = left_spaces+ "*" + hollow_spaces + "*"
#     print(row_output)

# first_row = (" "*(size_of_diamond-1)+"*")
# print(first_row) 
#######################################################

# #Coding Practice 17 #Problem1
# n = int(input())
# #first_row
# first_row = "* "*2*n
# print(first_row)
# for row in range(1, n):
#     first_spaces = "  "* (row*2)
#     rest_of_rows = ("* "*(n-row)) + (first_spaces) + ("* "*(n-row))
#     print(rest_of_rows)

# for row in range(1,n):
#     first_spaces = "  "*((n*2)-(row*2))
#     rest_of_rows = ("* "*(row)) + first_spaces + ("* "*(row))
#     print(rest_of_rows)
   
# first_row = "* "*2*n
# print(first_row)

####################################################
# n = int(input())
# for i in range(0, n):
#     row_out = " " * (n-i)
#     row_out = row_out + "$" * n
#     print(row_out)
####################################################
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     k = 1/i
#     sum = sum+k
# print(round(sum,2))
###################################################

# k = int(input())
# n = 2*k-1
# for row in range(1, k):
#     dots_row_left = ". "*(k-row)
#     dots_row_right = ". "*(k-row)
#     zeros_row = "0 "*(row)+"0 "*(row-1)
#     dots_row = dots_row_left+zeros_row+ dots_row_right
#     print(dots_row)

# for row in range(0, k):
#     dots_row_left = ". "*(row)
#     dots_row_right =". "*(row)
#     zeros_row = "0 "*(k-row)+"0 "*(k-row-1)
#     dots_row = dots_row_left+zeros_row+ dots_row_right
#     print(dots_row)
####################################################


# #a(x*2)+b(x)+c = 0
# The standard form of a quadratic equation is ax2 + bx + c = 0
# The discriminant of the quadratic equation is D = b2 - 4ac
# For D > 0 the roots are real and distinct.
# For D = 0 the roots are real and equal.
# For D < 0 the roots do not exist, or the roots are imaginar

# a = int(input())
# b = int(input())
# c = int(input())

# r1 = (-b+((b**2)-(4*a*c))**0.5)/(2*a)
# r2 = (-b-((b**2)-(4*a*c))**0.5)/(2*a)
# print(round(r1,2))
# print(round(r2,2))
#######################################################

# string = input("Enter the text: ")
# for i in range(len(string)):
#     order = ord(string[i])
#     order = int(order)
#     if order ==32:
#         order = 31
#     k = order+1
#     print(chr(k), end='')
    