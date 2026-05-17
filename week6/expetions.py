import random
# excesrise

# 1.
# def safe_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None
# 2.
# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "undefined"
# 3.
# def get_value(d,key):
#     try:
#         return d[key]
#     except KeyError :
#         return "mising"
# 4.
# def parse_ints(values):
#     int_list=[]
#     for num in values:
#         try:
#             int_list.append(num)
#         except ValueError:
#             continue
#     return int_list
# 5.
# def get_age(age):
#     if age<0 or age>150:
#         print("the age connot be anegative")
#         raise ValueError
#     return age
# 6.
# def func():
#     x=random.randint(0,10)
#     y=random.randint(0,10)
#     return x/y
# def retry(func,n):
#     while n>0:
#         try:
#             a=func()
#             return a
#         except :
#             n-=1
#             if n==0:
#              raise
# print(retry(func,3))
# 7.
# def count_erors(functions):
#     counter=0
#     for funci in functions:
#         try:
#             f=funci()
#         except Exception:
#             counter-=1
#     return counter
# 8.
def load_confing(path):

        try:
            with open (path) as f:
               inti=int(f.readline)
    
        
        except Exception as e:
           raise RuntimeError("conot int")from e
        # print(e)
        # print(e.__cause__)
print(load_confing("Untitled-1.txt"))



    


