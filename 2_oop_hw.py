# n1
class Auto:
    def __init__(self, n, c, cost, d, s):
        self.name=n
        self.color=c
        self.cost=cost
        self.distance=d
        self.speed=s

    def update_distance(self, n):
        self.distance=n
    
    def update_cost(self, n):
        self.cost=n
    

class Cars:
    def __init__(self):
        self.cars=[]
    
    def add_car(self, n):
        self.cars.append(n)
    
    def info(self):
        for i in self.cars:
            print(f"{i.name} {i.color} {i.cost} {i.distance} {i.speed}")
        
# a1=Auto('Cobalt', 'Oq', '$10_000', '100_000 km', '200 km/h')
# a2=Auto('Camry', 'Gray', '$55_000', '10_000 km', '350 km/h')
# cars=Cars()
# a1.update_distance('75_000 km')
# a2.update_cost('$45_000')
# cars.add_car(a1)
# cars.add_car(a2)
# cars.info()

# n2
class Restaurant:
    def __init__(self, time):
        self.work_time=time
        self.menu=[]
    
    def add_food(self, a):
        self.menu.append(a)
    
    def get_work_time(self):
        return f"{self.work_time}"
    
res = Restaurant("08:00 - 22:00")
res.add_food("Osh")
res.add_food("Lag'mon")
# print(res.get_work_time())

# n3
class User:
    def __init__(self, a,b):
        self.name=a
        self.surname=b
        self.followers=[]
        self.following=[]

    def follow(self, n):
        if n not in self.following:
            self.following.append(n)
            n.followers.append(self)

    def unfollow(self , n):
        if n in self.following:
            self.following.remove(n)
            n.followers.remove(self)

    def remove_follower(self, n):
        if n in self.followers:
            self.followers.remove(n)
            n.following.remove(self)

    def info(self):
        followers_names=[]
        for i in self.followers:
            followers_names.append(i.name)

        following_names=[]
        for i in self.following:
            following_names.append(i.name)

        print(f"--- {self.name} {self.surname} profili ---")
        print(f"(Followers): {followers_names}")
        print(f"(Following): {following_names}\n")

user1 = User("Ali", "Valiyev")
user2 = User("Vali", "Aliyev")
user3 = User("Olim", "Hakimov")

# user1.follow(user2)

# user3.follow(user2)

# user2.follow(user3)

# user1.info() 
# user2.info() 
# user3.info() 

# user1.unfollow(user2)
# user2.info()  

# n4
class Phone:
    def __init__(self, brand , model, price, year):
        self.brand=brand
        self.model=model
        self.price=price
        self.year=year
    
    def update_price(self, n):
        self.price=n
    
    # def info(self):
    #     print(f"{self.brand} {self.model} ${self.price} {self.year}")
    
p1=Phone('Iphone', '17 Pro Max', 2_000, '2025')
# p1.info()
# p1.update_price(1_300)
# p1.info()

# n5
class Employee:
    def __init__(self, name, surname, date, position, salary: int):
        self.name=name
        self.surname=surname
        self.date=date
        self.position=position
        self.salary=salary
        self.bonus=0

    def set_bonus(self):
        if int(self.salary) < 10_000_000:
            self.bonus=self.salary*0.25
    def info(self):
        print(f"Oylik: {self.salary} bonus: {self.bonus}")
    
e1=Employee('Max', 'Ford', '10-11-2024', "O'qituvchi", 8_000_000)
# e1.set_bonus()
# e1.info()

