# calculating area depending on the type of shape the user wants

shape = input("chose your shape:\n{circle,rectangle,square}: \n")
if shape=="circle":
    r = float(input("entre radius: "))
    pi = 3.14
    area = pi*r**2
    print(f"the area of a circle with radius {r} is",area)
elif shape=="rectangle":
    length = float(input(" enter length: "))
    width = float(input(" enter width: "))
    area = length*width
    print(f"the area of rectangle with length {length} and width {width} is",area)
elif shape=="square":
    sq = float(input("square: "))
    area = sq*sq
    print(f"the area of square {sq} is ",area)
else:
    print("please go back and chose an option")