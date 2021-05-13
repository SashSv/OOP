class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f" Rectangle ({rect_1.x} {rect_1.y} {rect_1.w} {rect_1.h})"

rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1)