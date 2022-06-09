# print('x', 'y', 'z', 'w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((not(x and y) or (not(z) or w)) and ((w or x) or not(y))):
#                     print(x, y, z, w)

# s = 0
# n = 0
# while s < 165:
#     s += 15
#     n += 2
# print(n)

# string = '1' + '8' * 99 + '1'
# while '81' in string or '882' in string or '8883' in string:
#     if '81' in string:
#         string = string.replace('81', '2', 1)
#     elif '882' in string:
#         string = string.replace('882', '3', 1)
#     else:
#         string = string.replace('8883', '1', 1)
# print(string)

# def F(n):
#     if n > 2:
#         return F(n-1)+ F(n-2)
#     else:
#         return 1
# print(F(6))


# file = open('17_11.txt')
# list_ = [int(i) for i in file]
# summ = 0
# quentity = 0
#
# for i in range(len(list_)):
#     for j in range(i, len(list_)):
#         if (list_[i] + list_[j]) % 9 == 0:
#             quentity += 1 
#             summ = max(summ, list_[i] + list_[j])
# print(quentity, summ)

# file_ = open('17_14.txt')
# list_ = [float(i) for i in file_]
# quentity = 0
# maxx_summ = 0
# s = 0
# count = 0
# for i in list_:
#     if i % 2 == 0:
#         s += i
#         count += 1
# sr = s / count
# for i in range(len(list_) - 1, 0, -1):
#     if (list_[i] % 3 == 0 or list_[i - 1] % 3 == 0) and (list_[i] < sr or list_[i - 1] < sr):
#         quentity += 1
#         maxx_summ = max(maxx_summ, list_[i] + list_[i - 1])
# print(quentity, maxx_summ)

