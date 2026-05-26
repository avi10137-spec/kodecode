# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def bark(self):
#         return self.name+" says woof"
# d1=Dog("rex")
# print(d1.bark())
# 2.
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
# r1=Rectangle(4,3)
# print(r1.area())
# 3.
# class Counter:
#     counter=0
#     def __init__(self):
#         pass
#     def incroment(self):
#         Counter.counter+=1
#     def value(self):
#         print(Counter.counter)
# c1=Counter()
# c1.incroment()
# c1.incroment()
# c1.value()
# 4.
# class Point:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return f"{self.a},{self.b}"
# p1=Point(1,2)
# print(p1)
# 5.
# class BankAccount:
#    def __init__(self,balance=10):
#        self.balance=balance
#    def deposit(self,amount):
#        self.balance+=amount
#        return self.balance
#    def withdraw(self,amount):
#        if amount < self.balance:
#            self.balance -= amount
#        return self.balance
# b1=BankAccount()
# print(b1.withdraw(8))
# class Temperture:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     def change_to_fhernhit(self):
#         return (self.celsius*1.8)+32
# t1=Temperture(100)
# print(t1.change_to_fhernhit())
# class Student:
#     def __init__(self,name,school="kodcode"):
#         self.name=name
#         self.school=school
# s1=Student("avi")
# s2=Student("dani")
# print(s1.name,s1.school)
# print(s2.name,s2.school)
# 8.
from collections import Counter


# class Player:
#     counter=0
#     def __init__(self):
#         Player.counter+=1
# p1=Player()
# p2=Player()
# print(p2.counter)
# 9.
# class Money:
#     def __init__(self,amount):
#         self.amount=amount
#     def is_more(self,other):
#         return other.amount < self.amount
# m1=Money(10)
# m2=Money(15)
# print(m1.is_more(m2))
# class Playlist:
#     def __init__(self,sings):
#         self.sings=sings
#
#
#     def add(self,title):
#         self.sings.append(title)
#         return self.sings
#     def remove(self,title):
#         self.sings.remove(title)
#         return self.sings
#     def count(self):
#         return len(self.sings)
#     def __str__(self):
#         return f"{" ".join(self.sings)}"
# p1=Playlist(["a","b","c"])
# print(p1)
# print(p1.add("d"))
# print(p1)
# print(p1.remove("a"))
# print(p1)
# print(p1.count())






