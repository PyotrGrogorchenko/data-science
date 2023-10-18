from Human import Human


class Teacher(Human):

    def __init__(self, name, gender, age):
        self.number_of_students = 0
        super().__init__(name, gender, age)

    def teach(self, material, students):
        self.number_of_students += len(students)
        for student in students:
            student.take(material)

