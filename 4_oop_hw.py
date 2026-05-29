#n1
class Student:
    def __init__(self, name, student_id):
        self.name=name
        self.sutdent_id=student_id
        self.__grades=[]
    
    def add_grade(self, grade):
        if 0<=grade<=100:
            self.__grades.append(grade)
        else:
            print("Noto'g'ri baho")
        
    def calculate_avg(self):
        return sum(self.__grades)/len(self.__grades)
    
    def get_status(self):
        avg=sum(self.__grades)/len(self.__grades)
        if 90<=avg<=100:
            return "A'lo"
        elif 80<=avg<=89:
            return "Yaxshi"
        elif 70<=avg<=79:
            return "Qoniqarli"
        elif avg<70:
            return "Qoniqarsiz"
        
# student=Student("Nodira", 'S123')
# student.add_grade(85)
# student.add_grade(90)
# print(student.calculate_avg())
# print(student.get_status())
# student.add_grade(150)

#n2
class Employee:
    def __init__(self, name, employee_id, hourly_rate=float):
        self.name=name
        self.employee_id=employee_id
        self.__working_hours=[]
        self.hourly_rate=hourly_rate

    def log_hours(self, hour):
        if 0<=hour<=24:
            self.__working_hours.append(hour)
            return True
        else:
            return False
    
    def total_hours(self):
        return sum(self.__working_hours)
    
    def calculate_salary(self):
        return sum(self.__working_hours)*self.hourly_rate
    
    def reset_hours(self):
        self.__working_hours.clear()

# employee = Employee("Javlon", "E101", hourly_rate=20.0)

# print(employee.log_hours(8))   	# True
# print(employee.log_hours(9))   	# True
# print(employee.log_hours(10))  	# True
# print(employee.log_hours(25))  	# False 

# print(employee.total_hours())       	# 27
# print(employee.calculate_salary())  	# 540.0 (27 * 20)

# employee.reset_hours()
# print(employee.total_hours())       	# 0
# print(employee.calculate_salary())  	# 0.0

#n3
class User:
    def __init__(self, username):
        self.username=username
        self.friends=[]

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            return True
        else:
            return False
        
    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            return True
        else:
            return False

    def list_friends(self):
        return self.friends

    def is_friend(self, friend):
        if friend in self.friends:
            return True
        else:
            return False
    
    def mutual_friends(self, other_user: 'User'):
        return list(set(self.friends).intersection(other_user.friends))
    
# user1 = User("Ali")
# user2 = User("Vali")

# print(user1.add_friend("Sami"))    # True
# print(user1.add_friend("Vali"))    # True
# print(user1.add_friend("Sami"))    # False (allaqachon mavjud)

# print(user2.add_friend("Ali"))     # True
# print(user2.add_friend("Sami"))    # True

# print(user1.list_friends())   # ['Sami', 'Vali']
# print(user2.list_friends())    # ['Ali', 'Sami']

# print(user1.is_friend("Vali"))     # True
# print(user1.is_friend("Botir"))    # False

# print(user1.mutual_friends(user2)) # ['Sami']

# print(user1.remove_friend("Vali")) # True
# print(user1.remove_friend("Botir"))# False
# print(user1.list_friends())        # ['Sami']