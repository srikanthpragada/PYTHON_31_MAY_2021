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


rect_list = [Rectangle(10, 20), Rectangle(10, 10), Rectangle(5, 10), Rectangle(5, 5)]

for r in sorted(rect_list):
    print(r)

print(Rectangle(10, 20) + Rectangle(20, 30))
