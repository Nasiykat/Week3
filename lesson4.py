# shop_cash = [10000,34000,30000,12300,4500,90000,78999]
# expenses = [1000,3000,2000,5000,5600,7654,3425]
# all_cash = sum(shop_cash)
# all_expenses = sum(expenses)
# profit = all_cash - all_expenses
# print(all_cash)
# print(all_expenses)
# print(profit)

# def get_money(shop_cash,expenses):
#     all_cash = sum(shop_cash)
#     all_expenses = sum(expenses)
#     profit = all_cash - all_expenses
#     return profit
# print(get_money(shop_cash,expenses))


#args **kwargs
# def get_arguments(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)

# get_arguments(1,2,3,"dffgh",{1,0}, name ="Nas", age = 38)

# def get_list_square(*args,**kwargs):
#     result = []
#     # dict = {}
#     if args:
#         for i in args:
#             result.append(i**2)
#     if kwargs:
#         for key,value in kwargs.items():
#             if type(value) == str:
#                 kwargs.update({
#                     key:value.upper()
#                 })
#             elif type(value) == set:
#                 kwargs.update({
#                     key: [value]
#                 })
#
#         return result, kwargs
# print(get_list_square(1,3,7,11,name = 'Nas', age = 38, sets ={1,3}))

# def get_max(a,b,c):
#     if a>b and a>c and b>c:
#         print(f"{a} is maximum")
#         print(f"{c} is minimum")
#     if b>a and b>c and a>c:
#         print(f"{b} is maximum")
#         print(f"{c} is minimum")
#     if c > a and c > b and a > b:
#             print(f"{c} is maximum")
#             print(f"{b} is minimum")
#
# print(get_max(7,9,3))




