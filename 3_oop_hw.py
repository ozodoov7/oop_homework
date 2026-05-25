class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Course:
    def __init__(self, course_name, course_teacher):
        self.course_name=course_name
        self.course_teacher=course_teacher
        self.cnt_students=0
        self.students=[]
    
    def add(self, new_student):
        if new_student not in self.students:
            self.students.append(new_student)
            self.cnt_students+=1
        else:
            print("Bu talaba allaqachon bor!")
        
    def delete(self, student):
        for i in self.students:
            if student.name == i.name:
                self.students.remove(i)
                self.cnt_students-=1

    def info_course(self):
        print(f"Kurs nomi: {self.course_name}")
        print(f"Kurs o'qituchisi: {self.course_teacher}")
        print(f"Talabalar soni: {self.cnt_students}")
        print("Talabalar: ")
        for i in self.students:
            print(f"{i.name} {i.age}")

# sinab ko'rish uchun n1
# n1=input("Kurs nomini kiriting: ")
# t1=input("O'qituvchi ismini kiriting: ")
# c1=Course(n1, t1)

# n=int(input("Nechta talaba qo'shildi? "))
# for i in range(n):
#     name=input(f"{i+1}-talaba ismini kiriting: ")
#     age=int(input("Bu talaba yoshini kiriting: "))
#     s=Student(name, age)
#     c1.add(s)

# r=int(input("Nechta talaba kursdan chetlashtirildi? "))
# for i in range(r):
#     s1=input("Talaba ismini kiriting: ")
#     c1.delete(s1)

# sinab ko'rish uchun n2
# c1=Course("Python_basics", 'Mirjamol aka')
# s1=Student('Doston', 20)
# s2=Student('Sardor', 19)
# s3=Student('Asilbek', 21)
# s4=Student('Shahzoda', 20)
# s5=Student('Madina', 19)
# s6=Student('Bekzod', 22)
# s7=Student('Javohir', 20)
# s8=Student('Kamola', 21)
# s9=Student('Jasur', 19)
# s10=Student('Laylo', 20)
# c1.add(s1)
# c1.add(s2)
# c1.add(s3)
# c1.add(s4)
# c1.add(s5)
# c1.add(s6)
# c1.add(s7)
# c1.add(s8)
# c1.add(s9)
# c1.add(s10)
# c1.delete(s1)
# c1.delete(s6)
# c1.info_course()

from translate import Translator

class Converter:
    def __init__(self, matn):
        self.gap=matn
    
    def ru_to_en(self):
        tarjimon=Translator(to_lang='en', from_lang='ru')
        new_gap=tarjimon.translate(self.gap)
        return new_gap
    
    def en_to_ru(self):
        tarjimon=Translator(to_lang='ru', from_lang='en')
        new_gap=tarjimon.translate(self.gap)
        return new_gap

# matn='привет'
# m='Good morning'
# c1=Converter(matn)
# print(c1.ru_to_en())
# c2=Converter(m)
# print(c2.en_to_ru())

# n3
class String:
    def __init__(self, matn):
        self.matn=matn
    
    def to_lower(self):
        result=''
        for i in self.matn:
            if 'A' <= i <='Z':
                result+=chr(ord(i)+32)
            else:
                result+=i
        return result
    
    def to_upper(self):
        result=''
        for i in self.matn:
            if 'a'<=i<='z':
                result+=chr(ord(i)-32)
            else:
                result+=i
        return result
    
    def is_upper(self):
        result=''
        for i in self.matn:
            if 'a'<=i<='z':
                return False
        return True
    
    def is_lower(self):
        result=''
        for i in self.matn:
            if 'A'<=i<='Z':
                return False
        return True
    
# my_string = String("Hello World 2026!")
# print(f"Asl matn: {my_string}")
# print(f"Kichik harflarda: {my_string.to_lower()}")
# print(f"Katta harflarda: {my_string.to_upper()}")

# print("-" * 30)

# str1 = String("python")
# str2 = String("PYTHON")
# str3 = String("12345") 

# print(f"'{str1.matn}' hammasi kichikmi?:", str1.is_lower()) 
# print(f"'{str2.matn}' hammasi kattami?:", str2.is_upper())  

# n4
class Taqvim:
    def __init__(self, date):
        self.date=date
    
    def hijriyga(self):
        if self.date>622:
            n=(self.date-622)*33/32
            return int(n)
    
    def grigoryanga(self):
        n=self.date*32/33+622
        return int(n)
    
# n=2026
# y=Taqvim(0)
# print(y.hijriyga())
# print(y.grigoryanga())