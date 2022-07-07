# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,5,4,6}
# print(set1.union(set2))
# s = {i**2 for i in range(4)}
# print(s)
# set1 ={1,2}
# set2 ={3}
# set3 ={4,5}
# set4 ={3,2,6}
# set5 ={6}
# set6 ={7,8}
# set7 ={9,8}
# print(set1.union(set4))
# print(set2.union(set4))
# print(set4.union(set5))
# print(set6.union(set7))

# set1 = {3,2,6}
# set2 = {1,2,3,5,6}
# set3 = {3,2,6}
# if set3.issuperset(set1):
#     print('is superset')
# else:
#     print("no super set")
# if set1 == set3:
#     print("equal")

# print(set1.issuperset(set2))
# print(set1.issubset(set2))


#comprehension  lists,dict
# lists = []
# for i in range(1,10):
#          lists.append(i)
# print(lists)
# lists = [i for i in range(1,10)]
# print(lists)
#
import datetime
# time_now = datetime.datetime.now()
# print(time_now)

# lists = []
# time_now = datetime.datetime.now()
# for i in range(1,10001):
#     lists.append(i)
# delta = datetime.datetime.now()-time_now
# print(delta)




# lists = [i for i in range(1,101) if i%2 == 0 and i%5 == 0]
# print(lists)

# num = int(input("Enter a number:"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
#  print(factorial)

# dicts = {i: i**2 for i in range(1,5)}
# print(dicts)
# lists = ["apple","banana","potato","tomato","melon"]
# dict = {i  : i*2 for i in lists}
# print(dict)
# dict1 = {
#    "a":1,
# "b":2
# }
#
# dict2 = {
#   "c":3,
# "d":4
#
# }
#
# dict3 = dict(zip(dict1,dict2))
# print(dict3)

import math
# def multiply(a,b,c):
#     if c == a*b:
#         print("Correct.")
#     else:
#         print(f"Incorrect. Correct answer is {a*b}")
# multiply(2,3,6)
#
# for i in range(1,11):
#     for j in range(1,11):
#         print('{:3d}'.format(i*j), end=' ')
#     print()

from random import choice
l = ['rock','paper','scissors']
name = input("Name:")
name = 1
comp = 1
computer = choice(l)
y = input("Your turn:")
if (y =='rock' and computer == 'paper') and (y == 'paper' and computer == 'scissors') and  (y == 'scissors' and computer == 'rock'):
    print("draw")
elif (y =='paper' and computer == 'rock') and (y == 'paper' and computer == 'scissorss') and  (y == 'scissors' and computer == 'rock'):
    print("win")
elif y =='rock' and computer == 'paper':
    print("loss")
print(computer)







