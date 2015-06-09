#!/usr/bin/python
def square(L):
    return L*L
def rectangle(width,height):
    return width*height
def circle(radius):
    return 3.14159*radius**2
def options():
    print()
    print("Options:")
    print("Press s: to calculate area of a square")
    print("Press c: to calculate area of a circle")
    print("Press r: to calculate area of a rectangle")
    print("Press q: to quit")
    print()
print("\n\t\tArea of Shapes")
choice="x"
options()
while choice!="q":
    choice=input("Enter your choice:")
    if choice=="s":
        L=float(input("Enter length of a square:"))
        print("Area of a square:",square(L))
        options()
    elif choice=="c":
        radius=float(input("Enter radius of a circle:"))
        print("Area of a circle:",circle(radius))
        options()
    elif choice=="r":
        width=float(input("Enter width:"))
        length=float(input("Enter Length:"))
        print("Area of a rectangle:",rectangle(width,length))
        options()
    /*elif choice=="q":
        print(" ",end="")*/
    else:
        print("Invalid choice")
        options()

