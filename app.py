class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if (len(self.students) < self.max_students):
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total_students = len(self.students)
        total_grades = 0
        for student in self.students:
            total_grades += student.get_grade()
        return total_grades / total_students

    def get_students(self):
        return self.students


uru = Student('Uru', 22, 90)    
natu = Student('Natu', 25, 90)
temp = Student('Temp', 20, 100)

course = Course('Python course', 2)
print(course.add_student(uru))
print(course.add_student(natu))
print(course.add_student(temp))
print(course.get_students())
print(course.get_average_grade())
