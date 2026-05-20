# class Animal:
#     def __init__(self, type, color, name):
#         self.name = name
#         self.color = color
#         self.type = type

#     def sound(self):
#         print("Animal is speaking...")

# # a1 = Animal("BullDog", 'black', 'rex')

# class Dog(Animal):
#     pass

# class Flyable:
#     def fly(self):
#         print("Flying...")

# class Swimable:
#     def swim(self):
#         print("Swimming...")


# class People:
#     def swim(self):
#         print("People can swim...")


# class Duck( Flyable, Swimable, People):
#     def run(self):
#         print("Running...")

# class Bird(Duck):
#     def fly(self):
#         print("Bird is flying...")

# bird1 =  Bird()
# bird1.fly()
# bird1.run()
# bird1.swim()

# class Animal:
#     def run(self):
#         print("Running...")
    
#     def eat(self):
#         print("Eating...")


# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# class Pinguin(Animal):
#     pass

# d1 = Dog()
# c1 = Cat()
# p1 = Pinguin()

# d1.eat()
# d1.run()

# c1.eat()
# c1.run()

# p1.eat()
# p1.eat()


# n1
class Animal:
    def __init__(self, n):
        self.name=n
    

class Dog(Animal):
    def sound(self):
        print("Woof")

d1=Dog("Rex")
# d1.sound()

# n2
class Transport:
    def __init__(self, model, year):
        self.model=model
        self.year=year

class Car(Transport):
    def __init__(self, model, year, c):
        super().__init__(model, year)
        self.color=c

    def info(self):
        print(f"{self.model} {self.year} {self.color}")

c1=Car("Gentra", "2025", "Qora")
# c1.info()

# n3
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, a,b,grade):
        super().__init__(a,b)
        self.grade=grade
    def show_info(self):
        print(f"{self.name} {self.age} {self.grade}")
    
s1=Student('Javohir', '20', '3')
# s1.show_info()

# n4
class Building:
    def __init__(self, address):
        self.address=address
class School(Building):
    def __init__(self, a, cnt):
        super().__init__(a)
        self.student_cnt=cnt
    def info(self):
        print(f"{self.address} \n{self.student_cnt}")

# a=input("Manzilni kiriting: ")
# n=input("O'quvchilar sonini kiriting: ")
# s1=School(a, n)
# s1.info()

# n5
class Device:
    def __init__(self, b):
        self.brand=b
class Phone(Device):
    def __init__(self, b, ram):
        super().__init__(b)
        self.ram=ram
    def info(self):
        print(f"{self.brand} {self.ram}")

t1=Phone("Samsung S23", "8 GB")
# t1.info()

# n6
class Food:
    def __init__(self, n):
        self.name=n
class Fruit(Food):
    def __init__(self, n, v):
        super().__init__(n)
        self.vitamine=v
    def info(self):
        print(f"{self.name} {self.vitamine}")

m1=Fruit( 'olma', 'D')
# m1.info()

# n7
class Worker:
    def __init__(self, n, s):
        self.full_name=n
        self.salary=s
    
class Programmer(Worker):
    def __init__(self, a,b, lang):
        super().__init__(a,b)
        self.language=lang

class Workers:
    def __init__(self):
        self.workers=[]
    def add_workers(self, n):
        self.workers.append(n)
    def info(self):
        for i in self.workers:
            print(f'{i.full_name} {i.salary} {i.language}')

w1=Programmer("Ozodov Javohir", '5000', 'Py')
w2=Programmer('Komiljanov Ilhom', '4000', 'Ai')
w3=Programmer('Nazarov Muhammad', '3500', 'Odam tili')

workers=Workers()

# workers.add_workers(w1)
# workers.add_workers(w2)
# workers.add_workers(w3)

# workers.info()

# n8
# class Vehicle:
#     def __init__(self, b, s):
#         self.brand=b
#         self.speed=s

# class Bike(Vehicle):
#     def __init__(self, b, s, w):
#         super().__init__(b, s)
#         self.weight=w
    
# class Bikes:
#     def __init__(self):
#         self.bikes=[]

#     def add_bikes(self, b):
#         self.bikes.append(b)

#     def show_info(self):
#         for i in self.bikes:
#             print(f"{i.brand} {i.speed} {i.weight}")

# b1=Bike('Ducati', '300 km/h', '250 kg')
# b2=Bike("Honda", '320 km/h','230 kg')
# bikes=Bikes()
# bikes.add_bikes(b1)
# bikes.add_bikes(b2)
# bikes.show_info()