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
#GCD PRoblem
# n = int(input())
# m = int(input())
# n_list =[]
# m_list =[]
# for i in range(1, n+1):
#     if n%i == 0:
#         n_list =n_list + [i]
# for i in range(1, m+1):
#     if m%i == 0:
#         m_list =m_list+[i]
# for i in n_list:
#     if i
#################################################
# programming_languages_list = ["Python", "Java", "Ruby", "C", "C++", "Go", "R", "JavaScript", "Swift", "PHP", "Kotlin", "Perl"]
# n = int(input())
# for i in range(1, n+1):
#     k = int(input())
#     print(programming_languages_list[k])
###################################################

# n = int(input())
# m = int(input())
# list_a=[n]
# print(list_a*m)
##################################################

# num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# n = int(input())
# empty_list = []
# for i in range(0, len(num_list)):
#     if n<num_list[i]:
#         empty_list.append(num_list[i])
# print(empty_list)

####################################################
# n = int(input())
# empty_list=[]
# for i in range(1, n+1):
#     k = input()
#     empty_list.append(k)
# print(empty_list)
##################################################

# n = int(input())
# empty_list = []
# for i in range(1, n+1):
#     k = input()
#     empty_list.append(k)
# m = empty_list[::-1]
# for i in m:
#     print(i)
#####################################################
# n = int(input())
# empty_list = []
# for i in range(1, n+1):
#     k = input()
#     empty_list.append(k)
# k =  empty_list[:3] + empty_list[-3:]
# print(k)
###################################################
n = int(input())
empty_list =[]
for i in range(1, n+1):
    k = int(input())
    empty_list.append(k)
print(empty_list)