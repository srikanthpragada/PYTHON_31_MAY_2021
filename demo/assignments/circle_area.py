# Accept radius of a circle and display Area and Circumference

radius = float(input("Enter the radius:"))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f'Area of the circle          :{area:10.2f}')
print(f'Circumference of the circle :{circumference:10.2f}')
