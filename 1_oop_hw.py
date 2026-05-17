# n1
# class Market:
#     def __init__(self, n, p, a):
#         self.name=n
#         self.price=p
#         self.amount=a
#     def __repr__(self):
#         return f"{self.name} {self.price} {self.amount}"
#     def to_buy(self, a, c):
#         if self.name.lower() == a.lower():
#             if c>0:   
#                 if self.amount<=0:
#                     print("Bu mahsulot tugagan")
#                     return
#                 if self.amount<c:
#                     print(f"{self.name} mahsulot yetarli emas!\n{self.amount} kg qolgan! ")
#                     self.amount=0
#                 else:
#                     self.amount-=c
#                     print(f"{c} kg {self.name} sotib olindi! ")
#             else:
#                 print("Miqdori musbat bo'lishi kerak")
#                 return
#     def lasts(self):
#         print(f"{self.name} {self.price} {self.amount}")
# products=[]
# print("Do'kondagi mahsulotlarni kiriting")
# n=int(input("Nechta turdagi mahsulot bor? "))
# for i in range(n):
#     product=input("Mahsulot nomini kiriting: ")
#     price=float(input("Mahsulot narxini kiriting: "))
#     amount=int(input("Do'kondagi mahsulot miqdorini kiriting (kg): "))
#     i=Market(product, price, amount)
#     products.append(i)
# print("Do'kondagi mahsulotlar nomi/narxi/miqdori")
# for i in products:
#     print(i)
# b=int(input("Nechta mahsulot sotib olasiz? "))
# for i in range(b):
#     p=input("Mahsulot nomini kiriting: ")
#     a=int(input("Miqodirini kiriting (kg): "))
#     for j in products:
#         j.to_buy(p,a)

# print("Do'konda qolgan mahsulotlar")
# for i in products:
#     i.lasts()


# n2
# class Book:
#     def __init__(self, t, a, p):
#         self.title=t
#         self.author=a
#         self.page=p
#     def short_info(self):
#         return f"{self.title} kitobini {self.author} yozgan, {self.page} sahifa bor"
#     def is_it_big(self):
#         if int(self.page)>300:
#             return True
#         else:
#             return False
        
# title=input("Kitob nomini kiriting: ")
# author=input("Kitob muallifini kiriting: ")
# page=input("Kitob sahifasini kiriting: ")

# b1=Book(title, author, page)
# info=b1.short_info()
# print(info)
# print(b1.is_it_big())

# n3
# class Car:
#     def __init__(self, model, year, speed):
#         self.model=model
#         self.year=year
#         self.speed=speed
#     def increase_speed(self):
#         self.speed+=10
#     def decrease_speed(self):
#         self.speed-=10
#     def info(self):
#         print(f"{self.model} {self.year} {self.speed} km/p")
    
# model=input("Mashina modelini kiriting: ")
# year=int(input("Ishlab chiqarilgan yilini kiriting: "))
# speed=int(input("Eng katta tezligini kiriting: "))
# car=Car(model, year, speed)
# car.increase_speed()
# car.increase_speed()
# car.increase_speed()
# car.decrease_speed()
# car.info()

# n4
# class Account:
#     def __init__(self, name):
#         self.name=name
#         self.balance=0
#     def add_deposit(self, d):
#         self.balance+=d
#     def get_money(self, m):
#         if self.balance < m:
#             print("Hisobda buncha mablag' yo'q")
#             return
#         else:
#             self.balance-=m
#     def calculation(self):
#         return f"{self.name} {self.balance}"

# name=input("Ismni kiriting: ")
# a1=Account(name)
# a1.add_deposit(1000)
# a1.get_money(400)
# print(a1.calculation())

# n6
# import math as m
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def perimetr(self):
#         return self.a+self.b+self.c
#     def yuza(self):
#         s=(self.a+self.b+self.c)/2
#         y=m.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
#         print(f"Yuza: {y}")

# a=3
# b=4
# c=5
# u1=Triangle(a,b,c)
# print(u1.perimetr())
# u1.yuza()

# n6
# class LC:
#     def __init__(self, name, duration):
#         self.name=name
#         self.duration=duration
#         self.students=[]
#     def add_students(self, name):
#         self.students.append(name)
#     def cnt_students(self):
#         return len(self.students)
# name=input("O'quv markaz nomini kiriting: ")
# duration=int(input("Davomiyligini kiriting (oy): "))
# lc1=LC(name, duration)
# s1=input("Talaba ismini kiriting: ")
# s2=input("Talaba ismini kiriting: ")
# s3=input("Talaba ismini kiriting: ")
# lc1.add_students(s1)
# lc1.add_students(s2)
# lc1.add_students(s3)
# print(lc1.cnt_students())

# n7
# class book:
#     def __init__(self, author, title):
#         self.author=author
#         self.title=title
# class Library:
#     def __init__(self):
#         self.books=[]
#     def add_book(self, n):
#         self.books.append(n)
#     def search(self, n):
#         if n in self.books:
#             return True
#         else:
#             return False
        
# b1=book('Qodiriy','Mehrobdan Chayon')
# b2=book("Cho'lpon", 'Ikki eshik orasida')
# l1=Library()
# l1.add_book(b1)
# l1.add_book(b2)
# print(l1.search(b1))
