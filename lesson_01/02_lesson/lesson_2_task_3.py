import math
def square(side):
    s = side ** 2
    return s
x = float(input("Сторона квадрата: "))
result = square(x)
rounded = math.ceil(result)
print(f"Площать квадрата: {rounded}")