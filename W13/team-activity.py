from math import pi

def compute_area_square(side):
    return side * side

def compute_area_circle(radius):
    return round(pi * radius * radius, 1)


action = None

while action != "quit":
    shape_type = input("What kind of shape do you have? (square/circle) ")
    action = shape_type
    if shape_type == "square":
        side = float(input("type a side of square: "))
        print(f"Area: {compute_area_square(side)}")
    
    if shape_type == "circle":
        side = float(input("type a radius of circle: "))
        print(f"Area: {compute_area_circle(side)}")
