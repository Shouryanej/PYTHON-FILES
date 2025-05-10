name = str(input('Write Your name: '))
biology = int(input('Write your marks in Bio: '))
math = int(input('Write your marks in Math: '))
english = int(input('Write your marks in English: '))

class Student:
    def __init__(self, name, biology, math, english):
        self.name = name
        self.biology = biology
        self.math = math
        self.english = english

    def get_average(self):
        average = (self.biology + self.math + self.english) / 3
        print(f"{self.name}'s average marks: {average:.2f}")

# Create object and print average
s1 = Student(name, biology, math, english)
s1.get_average()%