# nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100, 20, 20]
# n= int(input())
# print(nums_list.count(n))
#################################################
# nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# # Write your code here
# n = int(input())
# counter = nums_list.count(n)
# for i in range(counter):
#     nums_list.remove(n)
# print(nums_list)
##################################################
# Python 3: Fibonacci series up to n
# def fib(n):
#     fib_list = [0]
#     a, b = 0, 1
#     while a < n:
#          #print(a, end=' ')
#          a, b = b, a+b
#          fib_list += [a] 
#     #print()
#     #print(fib_list)
#     print(fib_list[m]) 
# m = int(input())    
# n = 1000
# fib(n)
############################################
# def fib(n):
#     fib_list = [0]
#     a,b = 0,1
#     for i in range(1, n+1):
#         a, b = b, a+b
#         fib_list+=[a]
#     print(fib_list[n])
# n = int(input())
# fib(n)
# #################################################
# n = int(input())
# num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# new_list =[]
# # Write your code here
# l = len(num_list)
# for i in range(0, l):
#     k = num_list[i][:-1]+(n,)
#     new_list+=[k]
# print(new_list)
#############################################
n = input()
n = n.split()
box = []
length = len(n)
for i in range(length):
    box += [int(n[i])]
print(box.count(15))
