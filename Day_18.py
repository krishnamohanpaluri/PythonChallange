# n = int(input())
# numbers = ""
# for i in range(1, n+1):
#     spaces = " "*(n-i)
#     numbers =numbers+" " + str(i)
#     total = spaces+numbers+" "
#     print(total)
# n = int(input())
# numbers = ""
# for i in range(1, n+1):
#     spaces = " "*(n-i)
#     numbers =numbers+" " + str(i)
#     total = spaces+numbers+" "
#     print(total)
# k = ""
# for i in range(1, n+1):
#     k = k + " "+str(i)
#     spaces = " "*i
#     total = k+spaces
#     print(total)

# n = int(input())
# for i in range(1, n+1):
#     spaces = " "*(n-i)
#     stars = "* "*i
#     total = spaces+stars
#     print(total)

# for i in range(1, n):
#     spaces = " "*i
#     stars1 = "*"
#     i= i+1
#     space = "  "*(n-i)

#     total = spaces+stars1+space
#     print(total)
##########################################################
# k = input()
# m = k.split()
# print(m[::-1])
#######################################################
# k = input()
# m = k.split()
# sum = 0
# for i in range(len(m)):
#     n = int(m[i])
#     sum = sum+n
# print(sum)
#######################################################
# k = input()
# m = k.split()
# for i in range (len(m)):
#     print(m[i][::-1]+" " ,end='')
#######################################################
# k = input()
# m = k.split()
# n = len(m)
# for i in range(1, n+1):
#     print(m[n-i]+" ", end='')
#####################################################
k = input()
m = k.split()
sum = 1
for i in range(len(m)):
    n = int(m[i])
    sum = sum*n
print(sum)
