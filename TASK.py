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

# print('x', 'y', 'z', 'w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((not (x and y) or (not(z) or w)) and ((w or x) or not(y))):
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
# list = list(int(i) for i in file)
# max_sum = 0
# quentity = 0
# for i in range(len(list)):
#     for j in range(i, len(list)):
#         if (list[i] + list[j]) % 9 == 0:
#             quentity += 1
#             max_sum = max(max_sum, list[i] + list[j])
# print(quentity, max_sum)


# for x in range(64, 511):
#     L = 0
#     M = 0
#     y = x
#     while y > 0:
#         M = M + 1
#         if y % 2 == 0:
#             L = L + (y % 8)
#         y = y // 8
#     if L == 10 and M == 3:
#         print(x)

# x = int(input())
# a, b = 0, 1
# while x > 0:
#     a = a+1
#     b = b*(x%1000)
#     x = x//1000
# print(a)
# print(b)

# file = open('zadanie24_2.txt')
# max_count = 0
# string = file.read()
# for i in range(len(string) - 1):
#     count = 0
#     if string[i] == 'L':
#         count += 1
#         for j in range(len(string)):
#             if string[i + j] == 'L':
#                 count += 1
#             else:
#                 max_count = max(max_count, count)
#                 break
# print(max_count)



# for i in range(185311, 185330):
#     count = 0
#     del_ = []
#     for j in range(1, 185330):
#         if i % j == 0:
#             count += 1
#             del_.append(j)
#     if count == 4:
#         print(i, del_, '\n')

# file = open('28138.txt')
# pamit_limit, count_user = file.readline().split()
# pamit_limit = int(pamit_limit)
# count_user = int(count_user)
# save_users = [int(i) for i in file.readlines()]
# save_users = sorted(save_users)
# print(pamit_limit, count_user, save_users)
# pamit = 0
# count = 0
# for i in save_users:
#     if pamit <= pamit_limit:
#        pamit += i
#        count += 1
#     else:
#         print(pamit_limit, pamit, '\n', count, i)
#         break


# file = open('27-B.txt')
# N = int(file.readline())
# print(N)
# list_number = [int(i) for i in file.readlines()]
# list_number = sorted(list_number)
# min_sum = []
# for i in range(N):
#     for j in range(N):
#         if j > i:
#             for y in range(N):
#                 if y > j:
#                     if (list_number[i] + list_number[j] + list_number[y]) % 3 == 0:
#                         min_sum.append(list_number[i] + list_number[j] + list_number[y])
#                         if len(min_sum) == 1000000:
#                             print(min(min_sum))
#                             break



# file_ = open('24_demo_1.txt').readline()
# count = 0
# max_count = 0
# for i in range(1, len(file_)):
#     if file_[i - 1] != file_[i]:
#         count += 1
#     else:
#         count += 1
#         max_count = max(max_count, count)
#         count = 0
# print(max_count)


# file_ = open('zadanie24_2 (1).txt').readline()
# count = 0
# max_count = 0
# for i in range(len(file_)):
#     if (file_[i] == 'L' and count % 3 == 0) or (file_[i] == 'D' and count % 3 == 1) or\
#             (file_[i] == 'R' and count % 3 == 2):
#         count += 1
#         max_count = max(max_count, count)
#     elif file_[i] == 'L':
#         count = 1
#     else:
#         count = 0
# print(max_count)


# file_ = open('24_1.txt').readline()
# set_ = {}
# for i in range(1, len(file_) - 1):
#     if file_[i - 1] == file_[i + 1]:
#         if file_[i] not in set_:
#             set_[file_[i]] = 1
#         else:
#             set_[file_[i]] += 1
# max_ = 0
# end_key = ''
#
# for i in set_:
#     if set_[i] > max_:
#         max_ = set_[i]
#         end_key = i
# print(end_key)