#                           Coding Practice-18
# n = int(input())
# cumulative_sum = 0
# for i in range(n):
#     k = int(input())
#     cumulative_sum += k
#     print(cumulative_sum)

#########################################################
# n = int(input())
# cumulative_avarage = 0
# for i in range(1, n+1):
#     k = int(input())
#     cumulative_avarage += k
#     j = cumulative_avarage/i
#     print(round(j, 3))
#####################################################
# string = input()
# string_store = ""
# for char in string:
#     string_store = char+char
#     print(string_store, end='')

######################################################
# string = input()
# substring = input()
# sub_index = 0
# for char in string:
#     if char == substring[sub_index]:
#         sub_index+=1
#     if sub_index == len(substring):
#         break
# if sub_index == len(substring):
#     print("Yes")
# else:
#     print("No")
###################################################
#n = int(input())
# for i in range(1, n+1):
#     spaces = " "*(n - i)
#     left_nums = ""
#     right_nums = ""
#     for j in range(1, i+1):
#         left_nums = str(j) + left_nums
#         right_nums = right_nums + str(j)
#     print(spaces + left_nums + right_nums)

#####################################################

# w = input()
# k=""
# for i in range(len(w)-1) :
#     word = (w[i]+ "-")
#     k = k+word
# print(k+w[len(w)-1], end='' )
#########################################################
# n = int(input())
# entered_numbers = 0
# for i in range(n):
#     k = int(input())
#     entered_numbers += k
#     if entered_numbers < k:
#         print(k)
#     else:
#         print(k)
########################################################
# n = int(input())
# for i in range(1,n+1):
#     f_spaces = " "*(n-i)
#     b_spaces = " "*(2*i-2)
#     b_slash = "\\"
#     f_slash = "/"
#     first_part = f_spaces+f_slash+b_spaces+b_slash
#     print(first_part)
# for i in range(0,n):
#     f_spaces = " "*i
#     b_spaces = " "*(2*(n-i)-2)
#     b_slash ="\\"
#     f_slash ="/"
#     total = f_spaces+b_slash+b_spaces+f_slash
#     print(total) 
##########################################################
# string = input()
# string_list = []
# for char in string:
#     string_list+=char
# print(string_list)
#######################################################33
print(2**38)