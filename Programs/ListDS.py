# Method 1
# l = [10,20,30,40]
# print(type(l))
#
# Method 2
# l1 = eval(input("Enter List"))
# print(type(l1))
# print(l1)
#
# Method 3
# l = list(range(0,11,2))
# print(type(l))
# print(l)
#
# Method 4
# s = "Yousaf"
# l =list(s)
# print(type(l))
# print(l)
#
# Method 5
# s = "Learning python is very easy"
# l = s.split()
# print(type(l))
# print(l)
#
# Method 6
# nested list
# l=[10,20,[30,40]]
# print(type(l))
# print(l)
#
# Accessing element of a list
# by index
# types
# +ve
# -ve
#
# l =  [10,20,30,40,50]
# # +ve: 0, 1, 2, 3, 4 (start index, end index-1)
# # -ve:-5,-4,-3,-2,-1 (start index, end index)
# print("Positive index: ",l[4])
# print("Negative Index: ",l[-1])
#
# l = [10,20,30,40,50,60,70,80,90,100]
# print(l[2::2])
#
# l = [10,20,30,40]
# print(l)
# l[2]=555
# print(l)
#
# l = [1,2,3,4,5,6,7,8,9,10,11]
# # i=0
# # while (i<len(l)):
# #     print(l[i])
# #     i = i + 1
#
# l = [1,2,3,4,5,6,7,8,9,10,11]
# for i in l:
#     print(i)
#
# l = [1,2,3,4,5,6,7,8,9,10,11]
# for i in l:
#     if i%2==0:
#         print(i)
# l = [1,2,3,4,5,6,7,8,9,10,11]
# for i in l:
#     if i%2==1:
#         print(i)
#
# l = [1,2,3,4,5,6,7,8,9,10,11]
# x=len(l)
# for i in range(x):
#     print(l[i], "is available at +ve index:",i,"and -ve index :",i-x)
#
# l = [1,2,2,3,5,6,6,8,9,9,9,9]
# print(l)
# print(l.count(1))
# print(l.count(2))
# print(l.count(3))
# print(l.count(6))
# print(l.count(9))
#
# l = [1,2,3,4,5,6,7,8,9,10,11]
# print(l.index(12))
#
# l = [1,2,3,4,5,6,7,8,9,10,11]
# print(40 in l)
#
# l = ['APPLE', 'CAT', 'DOG']
# print(l)
# l.append('LION')
# print(l)
#
# l = ['APPLE', 'CAT', 'DOG']
# l1 = ['YOUSAF','BUX']
# print(l)
# l.append('LION')
# print(l)
# l.remove('CAT')
# print(l)
# l.insert(1,'CAT')
# print(l)
#
# l.extend(l1)
# print(l)
# l.extend("Learning")
# print(l)
#
# remove
# pop
# l = [10,20,30,40]
# print(l.pop())
# print(l.remove(10))
# print(l.pop(1))
# print(l.pop(10))
#
# l = [40,10,20,70,50]
# l.reverse()
# print(l)
#
# l = [40,10,20,70,50]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
#
# l = ['a','b','z','d']
# l.sort()
# print(l)
#
# l1 = [1,2,3,4]
# l3=l1
# print(id(l1))
# print(id(l3))
# l1[2]=40
# print(l1)
# print(l3)
#
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l2.extend(l1[1:3])
# print(l2)
#
# l1 = [1,2,3,4]
# l2=l1.copy()
# print(id(l1))
# print(id(l2))
# l1[2]=33
# print(l1)
# print(l2)
#
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# #  + operator
# l3 = l1 + l2
# print(l3)
#
# l1 = [10,20,30,40]
# l2 = l1*3
# print(l2)
#
# list comparison
# l1 = ['Dog','Cat','Lion']
# l2 = ['Dog','Cat','Lion']
# l3 = ['Dog','CAT','Apple']
# print(l1==l2)
# print(l1==l3)
# print(l2!=l3)
#
# l = [1,2,3,4,5,6,7,8,9]
# print(21 in l)
# l.clear()
# print(l)
#
# l = [10,20,[30,40]]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[2][0])
# print(l[2][1])
#
# l = [i*i for i in range(1,11)]
# print(l)
# l1 = [2**i for i in range(1,6)]
# print(l1)
# l2 = [i for i in l if i%2==0]
# print(l2)

s = "a quick brown fox jumps over the lazy dog".split()
print(s)
l = [[w.upper(), len(w)] for w in s]
print(l)












