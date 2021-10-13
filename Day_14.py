######################Coding Practice_13############
#p1&2 Prime Numbers from 1 to N

 
# m = int(input()) 
  
# for i in range(1, m+1):
#   if i>1:
#     for j in range(2,i):
#         if(i % j==0):
#             break
#     else:
#         print(i)

#############p3##########################
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(str(j)+" ", end= '')
#     print()

#################p4#########################
# n = int(input())
# for i in range(0, n):
#     for i in range(0, n-i):
#         print(str(i+1)+" ", end ='')
#     print()
#################p5#########################
# n = int(input())
# for i in range(n):
#     for row_num in range(i,n):
#          print((str(n-row_num))+" ", end='')
#     print()
#############################################
# limit=int(input("Enter upper limit:"))
# c=0
# m=2
# count = 0
# while(c<limit):
#     for n in range(1,m+1):
#         a=m*m-n*n
#         b=2*m*n
#         c=m*m+n*n
#         if(c>limit):
#             break
#         if(a==0 or b==0 or c==0):
#             break
#         count = count+1
#     m=m+1
# print(count)
# from typing import Counter


# n = int(input())
# count = 0
# for i in range(n+1):
#     i = (i+1)**2
#     for j in range(n-i):
#         j = (j+1)**2
#         for k in range(n):
#             k = (k+1)**2
#             if i + j == k:
#                 count = count+1
# print(count)
################################################
n = int(input())
k = int(input())
for i in range(k):
    for j in range (n+2):   
        print(str(n+j)+" ", end='')
    print()