from rectangle_1 import Rectangle, Square, Krug

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square(),
      square_2.get_area_square())

krug_1 = Krug(4)
krug_2 = Krug(8)
print(krug_1.get_krug_sq(),
      krug_2.get_krug_sq())

figures = [rect_1, rect_2, square_1, square_2, krug_1, krug_2]

for i in figures:
    if isinstance (i, Square):
        print(i.get_area_square())
    elif isinstance (i, Krug):
        print(i.get_krug_sq())
    else:
	    print(i.get_area())
