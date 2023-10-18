from Student import Student
from Teacher import Teacher
from Materials import Materials

materials = Materials(['Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers'])

teacher = Teacher('Galina Ivanovna', 'male', 52)

sergio = Student('Sergio', 'male', 25)
john = Student('John', 'male', 34)
karen = Student('Karen', 'female', 23)
kos = Student('Kos', 'male', 38)
masha = Student('Masha', 'female', 27)

for material in materials.get_materials():
    teacher.teach(material, [sergio, john, karen, kos, masha])

john.print_knowledge()
print(len(john))
john.lose()
john.print_knowledge()
print(len(john))
