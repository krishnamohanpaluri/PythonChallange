# n = int(input())
# a = 1
# for i in range(n):
#    space = ""
#    for j in range(i+1):
#       space = space + str(a)+" "
#       a+=1 #########
###########################################################
#GCD
# n = int(input())
# m = int(input())
# a = 0
# b = 0
# for i in range(1, n):
#    if n%(n-i) == 0:
#       a = a + i   
# for j in range(1,m):
#    if m%(m-i) == 0:
#       b = b+ j
# if a == b:
#    print(a)
################################################
# n = int(input())
# for i in range(n+1):
#    print("* "*(n-i))
#########################################################
# n = int(input())
# for i in range(n):
#    space = " "*i
#    star = "* "*(n-i)
#    pattern = space + star
#    print(pattern)
#####################################################
# n = int(input())
# for i in range(1, n+1):
#    for j in range(1,n+1):
#       print(str(j)+" ", end='')
###################################################
# n = input()
# n = n.split()
# box = []
# for i in range(len(n)):
#    box.append(int(n[i]))
# box = set(box)
# box = list(box)
# box.sort()
# print(box)
######################################################
# num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# # Write your code here
# n = input()
# n = n.split()
# box = []
# for i in range(len(n)):
#    box.append(int(n[i]))
# box = set(box)
# print(box)
# # n = set(n)
# # print(n)
#######################################################
# num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# # Write your code here
# n = input()
# n = n.split()
# box = []
# for i in range(len(n)):
#    box.append(int(n[i]))
# box = set(box)
# dif = num_set.difference(box)
# dif = list(dif)
# dif = sorted(dif)
# print(dif)
#######################################################
# first_line = input()
# first_line = first_line.split(",")
# second_line = input()
# second_line = second_line.split(",")
# box_1 = []
# box_2 = []
# for i in range(len(first_line)):
#    box_1.append(int(first_line[i]))
# for i in range(len(second_line)):
#    box_2.append(int(second_line[i]))
# box_1 = set(box_1)
# box_2 = set(box_2)
# result = box_1 & box_2
# result = list(result)
# result = sorted(result)
# print(box_1)
# print(box_2)
# print(result)
################################################
# n = int(input())
# multiples_of_2 = []
# multiples_of_3 = []

# for i in range(1, n+1):
#    a = i*2
#    multiples_of_2.append(a)
# for i in range(1, n+1):
#    b = i*3
#    multiples_of_3.append(b)
# multiples_of_2 = set(multiples_of_2)
# multiples_of_3 = set(multiples_of_3)
# first_output = multiples_of_2.difference(multiples_of_3)
# first_output = list(first_output)
# first_output = sorted(first_output)
# second_output = multiples_of_2.symmetric_difference(multiples_of_3)
# second_output = list(second_output)
# second_output = sorted(second_output)
# print(first_output)
# print(second_output)
# print(multiples_of_2)
# print(multiples_of_3)
###########################################################
# str_a = input()
# a = str_a.split(",")
# i = 0
# for item in a:
#     a[i] = int(item)
#     i += 1
# print(a)
######################################################3\
# set_a = {"pencil"}

# word = input()
# set_a.update([word])

# list_a = list(set_a)
# list_a = sorted(list_a)
# print(list_a)
###################################################
# n = input()
# n = n.split()
# box = []
# for i in range(len(n)):
#    box.append(int(n[i]))
# box = set(box)
# box = list(box)
# box = sorted(box)
# print(box)
##################################################
# n = input()
# n  =n.split(",")
# numbers = []
# for i in range(len(n)):
#    if n[i].isdigit():
#       numbers.append(n[i])
# box = []
# for i in range(len(numbers)):
#    box.append(int(numbers[i]))
# print(box)
##########################################
# numbers = input()
# numbers = numbers.split()
# box_1 = []
# box_2 = []
# for i in range(len(numbers)):
#    box_1.append(int(numbers[i]))
# box_1 = sorted(box_1)
# #print(box_1)
# #print(box_1[-1:])
# x = len(box_1)
# a = int(box_1[(x-1)])
# #print(a)
# for i in range(1, a+1):
#    box_2.append(i)
# #print(box_2)
# box_1 = set(box_1)
# box_2 = set(box_2)
# box_3 = box_2.difference(box_1)
# box_3 = list(box_3)
# box_3 = sorted(box_3)
# print(box_3)
###############################################################