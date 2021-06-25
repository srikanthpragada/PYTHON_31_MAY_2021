class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"{self.length} X {self.width}"

    def area(self):
        return self.length * self.width

    def __lt__(self, other):
        # print(self, other)
        return self.area() < other.area()

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)

    def __float__(self):
        return self.area() * 1.0


rect_list = [Rectangle(10, 20), Rectangle(10, 10), Rectangle(5, 10), Rectangle(5, 5)]

for r in sorted(rect_list):
    print(r)

r1 = Rectangle(10, 20)
r2 = Rectangle(20, 30)
print(r1 + r2)  # r1.__add__(r2)
print(float(r1) + float(r2))
