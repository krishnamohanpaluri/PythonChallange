# def compute_factorial(n):
#     # Complete this recursive function
#     if n == 1:
#         return 1
#     return n*(compute_factorial(n-1))
   

# num = int(input())
# # Call the compute_factorial function
# result =  compute_factorial(num)
# print(result)
#####################################################
# def sum_of_the_digits(number):
#     # Complete this recursive function
#     total = 0
#     for i in number:
#         total = total + int(i) 
#     print(total) 

# number = input()
# # Call the sum_of_the_digits function
# sum_of_the_digits(number)
#####################################################
# def sum_of_numbers(n):
#     if n == 0:  # Base case
#         return 0
#     else:
#         return n + sum_of_numbers(n-1)  # Recursion
# num = int(input())
# result = sum_of_numbers(num)
# print(result)
####################################################
# nums_list = [10, 20, 40, 50, 60]
# i = int(input())
# n = int(input())
# nums_list.insert(i,n)
# print(nums_list)
#################################################
#programming_languages = ['Python', 'C', 'Java', 'Ruby', 'C++', 'CSS', 'HTML', 'Bash', 'Perl', 'R', 'Swift', 'SQL', 'PHP', 'JavaScript']
# Write your code here
# l = len(programming_languages)
# k = int(input())
# for i in range(1, l):
#     programming_languages.pop(l-k)
#     print(programming_languages)
#########################################################
# def number_of_cars_needed(no_of_people):
#     # Complete this function
#     no_cars = no_of_people /5
#     if no_of_people /5 == 1:
#         print(1)
#     cars = int(no_cars)
#     if cars<no_cars:
#         no_cars = int(no_cars) +1
#         k = int(no_cars)
#         print(k)
# no_of_people = int(input())
# # Call the number_of_cars_needed function
# number_of_cars_needed(no_of_people)