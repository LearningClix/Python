
# String Data Type:

s = "Learning Clix" # String

#Define

# s1 = 'Learning Clix'
# s2 = "Learning Clix"
# s3 = '''This Channel beongs to
#         Learning Clix
#       '''
# s4 = """This Channel beongs to
#         Learning Clix """
# s5 = 'ch'
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)

#My name is 'Yousaf Bux'

# How we access string characters

#1. through index
#2. via slicing


#
# i=0
# for ch in s:
#     print('On index ',i, 'the char is ',ch)
#     i=i+1


# s[start index: end index-1: step]
# print(s[0:13])
#
# print(s[0])
#- indexing

# s = 'Learning Clix'
#
# #s[start Index: end index-1: step]
# print(s[0:13:1])
# #s[start index: end index +1: step]
# print(s[-1:-14:-1])

# Metimetical operators apply on string
# + used to concatenate 2 string
# * used to append same string
# s= "Learning"
# s1 = "Clix"
#
# print(s*3)
# s = "Learning Clix"
# s1 = "Learning Clix"

#comparison operator <,> <=,>=
#equality operators ==, !=

#comparison will be based on alphabetical order
#
# s1 = input("Enter fisrt string : ")
# s2 = input("Enter second string : ")
# if (s1 > s2):
#     print("First string is greater")
# else:
#     print("Second string is greater")

# remove spaces from a given string
#rstrip => romoved space from right
#lstrip => remobved spaces from left
#strip => rmoves space from both sides
# s = input("Enter your name : ")
# if s.strip() == "Yousaf":
#     print("Yousaf")
# else:
#     print("others..")
# count
# s="Learning Python Is Difficult"
#
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# s = 'Learning Clix'
#
# print(s.startswith('Learn'))
# print(s.endswith('n'))

s = 'LearningClix'
n='1234'
print(s.isalpha())
print(n.isalnum())
print(n.isdigit())
print(s.islower())
print(s.isupper())


