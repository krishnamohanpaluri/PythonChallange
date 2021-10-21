# # n = input()
# # m = n.split()
# # big = 0
# # for i in range(1, len(m)):
# #     j = int(m[(i-1)])
# #     k = int(m[i])
# #     if j<k:
# #         big = k
# #     else:
# #         big = j

# # print(big)
# ########################################################
# # n = input()
# # m = n.split()
# # sum = 0
# # for i in range(len(m)):
# #     k = int(m[i])
# #     sum = sum +k
# # avg = sum/(len(m))
# # print(round(avg, 2))
# #####################################################
# # string = input()
# # string_list = string.split()
# # print(string_list)
# # leng_string_list = len(string_list)
# # for i in range(0, leng_string_list-1):
# #     k = string_list[i]        
# #     print(k[0]+".",end='')
# # l = string_list[(leng_string_list-1)]
# # print(l[0])
# ######################################################
# # def count_of_lowercase_and_uppercase_letters(arg_1):
# #     uppercount = 0
# #     lowercount = 0
# #     for i in range(len(arg_1)):
# #         k = arg_1[i].isupper()
# #         if k == True:
# #             uppercount += 1
# #         else:
# #             lowercount+=1
# #     print(uppercount)
# #     print(lowercount)
# # word = input()
# # count_of_lowercase_and_uppercase_letters(word)
# ##########################################################
# def calculate_league_points(wins, draws, losses):
#     # Complete this function
#     total_points = ((wins*4)+(draws*2)-(losses*1))
#     print(total_points)

# statistics = input().split(",")
# wins = int(statistics[0])
# draws = int(statistics[1])
# losses = int(statistics[2])
# # Call the calculate_league_points function
# calculate_league_points(wins,draws,losses)
###########################################################
# def sum_of_squares_m_to_n(m, n):
#     # Complete this function
#     sum_of_squares  = 0
#     for i in range(m, n+1):
#         k = i**2
#         sum_of_squares += k
#     print(sum_of_squares)

# m = int(input())
# n = int(input())
# # Call the sum_of_squares_m_to_n function
# sum_of_squares_m_to_n(m,n)
# ############################################################
# def sum_of_cubes_m_to_n(m, n):
#     # Complete this function
#     sum_of_cubes  = 0
#     for i in range(m, n+1):
#         k = i**3
#         sum_of_cubes += k
#     print(sum_of_cubes)

# m = int(input())
# n = int(input())
# # Call the sum_of_cubes_m_to_n function
# sum_of_cubes_m_to_n(m,n)
#######################################################

# def show_numbers(number):
#     # Complete this Function
    
#     for i in range(number):
#         if i%2 == 0:
#             print(str(i)+ " EVEN")
#         else:
#             print(str(i)+" ODD")

# number = int(input())
# # Call the show_numbers function
# show_numbers(number)
#####################################################
from typing import NamedTuple


# def get_lower_and_upper_case_letters(word):
#     # Complete this function
#     uppercase = []
#     lowercase = []
#     for i in word:
#         k = i.isupper()
#         l = i.islower()
#         if k == True:
#             uppercase = uppercase+[i]
#         else:
#             lowercase = lowercase + [i]
#     for i in range(len(uppercase)):
#         print(uppercase[i], end='')
#     print()
#     for i in range(len(lowercase)):
#         print(lowercase[i], end='')
# word = input()
# # Call the get_lower_and_upper_case_letters function
# get_lower_and_upper_case_letters(word)
####################################################
# def count_the_vowels(word):
#     # Complete this function
#     vowels = "aeiou"
#     count = 0
#     for i in word:
#         for j in vowels:
#             if i == j:
#                  count +=1       
#     print(count)

# word = input()
# # Call the count_the_vowels function
# count_the_vowels(word)
#########################################################

# numbers = input()
# numbers = numbers.split(",")
# empty_list = []
# for i in range(len(numbers)):
#     k = int(numbers[i])
#     empty_list = empty_list+[k]
# print(max(empty_list))
#########################################################
# numbers = input()
# a = int(input())
# numbers = numbers.split(",")
# box = []
# for i in numbers:
#     k = int(i)
#     box = box + [k]
# m = sorted(box, reverse= True)
# print(m[(a-1)])
#numbers = sorted(numbers, reverse=True)
#print(numbers)
###########################################################
# string = input()
# box = []
# for i in string:
#     k = i.isdigit()
#     if k == True:
#         box = box+[i]
# n = sorted(box)
# m = sorted(box, reverse=True)
# sum = 0
# for i in range(0, len(n)):
#     sum = sum +int(n[i])
# print(sum)
# print(n[0])
# print(m[0])
##########################################################
