# # def char_freq(string_1):
# #     string_1= string_1.lower()
# #     unitq_chars = set(string_1)
# #     unitq_chars.discard(' ')
# #     unitq_chars = sorted(unitq_chars)
# #     for i in unitq_chars:
# #         msg = "{}: {}"
# #         print(msg.format(i, string_1.count(i)))
# #         # print(i)
# #         # print(string_1.count(i))

# # string_1 = input()
# # char_freq(string_1)
# # ###################################################\
# # def conversion(list_2):
# #     list_3 = []
# #     for i in list_2:
# #         i = int(i)
# #         list_3.append(i)
# #     return list_3

# # n = int(input())
# # list_1 = []

# # for i in range(n):
# #     list_2 = input().split()
# #     list_2 = conversion(list_2)
# #     list_1.append(list_2)
# # print(list_1)
# ###############################################
# n = input()
# n = n.split(",")
# m = int(input())
# box = []
# for i in range(len(n)):
#     box.append(int(n[i]))
# print(box)