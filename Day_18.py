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
n = int(input())
empty_list = []
for i in range(1, n+1):
    k = input()
    empty_list.append(k)
for i in range (len(empty_list)):
    print(empty_list[i])
