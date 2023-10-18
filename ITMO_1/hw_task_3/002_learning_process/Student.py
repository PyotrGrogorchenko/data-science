import random as rand

from Human import Human


class Student(Human):
    def __init__(self, name, gender, age):
        self.knowledge = []
        super().__init__(name, gender, age)

    def __len__(self):
        return len(self.knowledge)

    def take(self, material):
        if material not in self.knowledge:
            self.knowledge.append(material)

    def lose(self):
        if len(self.knowledge) == 0:
            return
        lost = rand.randint(1, len(self.knowledge))
        self.knowledge = list(filter(lambda k: self.knowledge[lost] != k, self.knowledge))

    def print_knowledge(self):
        print('knowledge of student:', self.name)
        print(', '.join(self.knowledge))