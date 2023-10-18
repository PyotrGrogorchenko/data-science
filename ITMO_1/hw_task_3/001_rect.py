class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2


rect = Rect(2, 3)
print(rect.area())
print(rect.perimeter())
