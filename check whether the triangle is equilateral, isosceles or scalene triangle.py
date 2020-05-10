a=int (input("Enter first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))
if (a==b==c):
    print("This triangle is equilateral triangle")
elif(a==b or a==c or b==c):
    print("This triangle is isosceles triangle")
else:
    print("This triangle is scalene triangle")