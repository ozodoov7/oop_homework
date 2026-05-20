import os
os.system("cls")
# class Car:
#     # brand = 'BMW'
#     # model = "M8"
#     # price = 200000
#     # color = 'black'
#     def __init__(self, b,m,p,c):
#         self.brand = b
#         self.model = m
#         self.price = p
#         self.color = c

#     def show_info(self):
#         print(f"{self.brand} {self.model} {self.price} {self.color}")

#     def change_price(self, new):
#         self.price = new

# car1 = Car('BMW', 'M8', 200000, 'black')
# # print(car1.brand)
# # print(car1.model)
# car1.show_info()
# car1.change_price(150000)
# car1.show_info()

# car2 = Car('GM', 'Damas', 7000, 'White')
# car2.show_info()
# car2.change_price(300000)
# car2.show_info()

# n1
# class Student:
#     def __init__(self, i, f, y, b):
#         self.ism = i.title()
#         self.familiya = f.title()
#         self.yonalish = y.title()
#         self.bosqich = b
#     def show_info(self):
#         print(f"{self.ism} {self.familiya} {self.yonalish} {self.bosqich}")
#     def check_exam(self, score):
#         if score >= 70:
#             print("Siz imtihondan o'tdingiz")
#             self.bosqich+=1
#             print(f"Sizning bosqichingiz oshdi: {self.bosqich}")
#         else:
#             print("Siz imtihondan o'tolmadingiz")
            
# name=input("Ismni kiriting: ")
# sname=input("Familyani kiriting: ")
# yonalish=input("Yo'nalishni kiriting: ")
# level=input("Boshqichni kiriting: ")
# score=int(input("Ballni kiriting: "))

# t1=Student(name, sname, yonalish, level)
# n2
# t1.show_info()
# t1.check_exam(score)

# n3
# class Market:
#     def __init__(self, user: str):
#         self.name=user
#         self.products={}
    
#     def add_product(self, product, price):
#         if product in self.products:
#             print("Bu mahsulot savatda bor!")
#         else:
#             self.products[product]=price
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.pop(product)
#             print("Mahsulot o'chirildi")
#         else:
#             print("Bunday mahsulot savatda yo'q")
#     def order(self):
#         for i in self.products:
#             print(i, self.products[i])
#         a=sum(self.products.values())
#         print(a)

# name=input('Foydalanuvchi ismini kiriting: ')
# u1=Market(name)
# a='y'
# while a=='y':
#     product=input("Qanaqa mahsulot kiritasiz: ")
#     price=int(input("Narxini kiriting: "))
#     u1.add_product(product, price)
#     a=input("Yana mahsulot qo'shasizmi? \n y/n?")
#     a=a.lower()

# a='y'
# while a=='y':
#     product=input("Qaysi mahsulotni o'chirasiz: ")
#     u1.remove_product(product)
#     a=input("Yana mahsulot o'chirasizmi? \n y/n?")
#     a=a.lower()

# u1.order()

# n4
# class Car:
#     def __init__(self, m, y, c):
#         self.model=m
#         self.year=y
#         self.passengers=c
#     def add_passenger(self):
#         self.passengers+=1
#     def drop_passenger(self):
#         self.passengers-=1
#     def show_info(self):
#         print(f"{self.model} {self.year} {self.passengers}")

# model=input("Mashina nomini kiriting: ")
# year=input("Mashina yilini kiriting: ")
# cnt=int(input("Yo'lovchilar sonini kiriting: "))
# c1=Car(model, year, cnt)
# c1.add_passenger()
# c1.add_passenger()
# c1.drop_passenger()
# c1.show_info()

# n5
# class Books:
#     def __init__(self, t, a, p):
#         self.title = t
#         self.author = a
#         self.page = p
#     def info(self):
#         print(f"{self.title} {self.author} {self.page}")
# b1=Books("Kecha va Kunduz", "Cho'lpon", 350)
# b1.info()

# n6
# class Student:
#     def __init__(self, n, l, s):
#         self.name = n
#         self.level = l
#         self.score = s
#     def add_score(self, n):
#         if self.score > 100:
#             print("Ball 100 dan oshmasligi kerak")
#         else:
#             self.score+=n
#     def info(self):
#         print(f"Ism: {self.name} \nKurs: {self.level} \nBall: {self.score}")

# s=Student("Javohir", 3, 80)
# s.add_score(10)
# s.add_score(5)
# s.info()

# import turtle
# class Architect:
#     def triangle(self, n):
#         turtle.pensize(4)
#         turtle.color("purple")
#         for i in range(3):
#             turtle.forward(n)
#             turtle.right(120)
#         turtle.done()
    
#     def rectangle(self, n, m):
#         turtle.pensize(3)
#         turtle.color("Black")
#         for i in range(4):
#             if i%2==0:
#                 turtle.forward(n)
#                 turtle.right(90)
#             else:
#                 turtle.forward(m)
#                 turtle.right(90)
#         turtle.done()

#     def circle(self, n):
#         turtle.pensize(3)
#         turtle.color("Black")
#         turtle.circle(n)
#         turtle.done()

# t1=Architect()
# # t1.triangle(200)
# t1.rectangle(100, 200)
# t1.circle(100)