# Construct a class hierarchy for people on a college campus. Include faculty, staff, and students. 
# What do they have in common? What distinguishes them from one another?

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}, and I am a {self.__class__.__name__}.")

class Faculty(Person):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)

        self.department = department

    def introduce(self):
        super().introduce()
        print(f"I am a faculty member in the {self.department} department.")

class Staff(Person):
    def __init__(self, name, age, gender, role):
        super().__init__(name, age, gender)
        self.role = role

    def introduce(self):
        return super().introduce()
        print(f"I am a {self.role} on campus.")

class Student(Person):
    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major

    def introduce(self):
        super().introduce()
        print(f"I am a {self.major} major at the college.")

# Create instances of the classes and demonstrate their behavior

faculty_member = Faculty("John Smith", 40, "Male", "Computer Science")
faculty_member.introduce()

staff_member = Staff("Jane Doe", 35, "Female", "Administrative Assistant")
staff_member.introduce()

student = Student("Alice Johnson", 20, "Female", "Biology")
student.introduce()
        
