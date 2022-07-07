# #function
# def test_func():
#     print("Hi")
# test_func()
    # pass

# summ = int(input("sum:"))
# year = int(input("year:"))
# interest = float(input("interest:"))
# amount = (year * summ * interest)/100 + summ
# print(amount)

# def total_amount(summ,year,interest):
#     amount = (year * summ * interest) / 100 + summ
#     print(amount)
#     return amount
#
# cash = total_amount(1000,2,10)

# def compound_interest(initial,year):
#     amount = initial*(1.1)**year
#     print(amount)
#     return amount
# cash = compound_interest(100.78,3)
# print(cash)
# def multiply(a,b,c):
#     if c == a*b:
#         print("correct")
#     else:
#         print(f"Incorrect. Answer is {a*b}")
# multiply(3,3,19)

# from random import randint
# num = int(input("Enter a number:"))
# for i in range(num):
#     print(randint(1,9), end="")

# from random import randint
# i =0
# while i < 3:
#     num = int(input("Enter a number:"))
#     for i in range(num):
#         print(randint(1,9), end="")

# import random
# def random_ndigits(ndigits):
#     min_num = 10**(ndigits - 1)
#     max_num = (10**ndigits) - 1
#     if ndigits == 1:
#         min_num = 0
#     return random.randint(min_num, max_num)
# print(random_ndigits(4))

# lists = []
# count = 0
# tik_tak = [["o",0,"x"],[0,0,"x"],["x", 0,"0"]]
# for i in range(len(tik_tak)):
#     for j in range(len(tik_tak)):
#         # print(j)
#         if tik_tak[i][j] == 0:
#             lists.append((i,j))
# print(lists)

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
#
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#
#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
        print("  Your ticket is $15.")



