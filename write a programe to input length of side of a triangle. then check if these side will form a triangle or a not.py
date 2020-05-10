a=float(input("Enter the first side of triangle:"))
b=float(input("Enter the second side of triangle:"))
c=float(input("Enter the third side of triangle:"))
if (a+b>c) and (b+c>a) and (c+a>b):
    print ("These sides form a triangle")
else :
    print ("These sides form not a triangle")
