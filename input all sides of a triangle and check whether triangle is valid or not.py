a=int(input("Enter any first side of triangle:"))
b=int(input("Enter any second side of triangle:"))
c=int(input("Enter any second side of triangle:"))
if (a+b>c):
    if(a+c>b):
        if(a<b+c):
            print("This triangle is valid")
        else:
            print("This triangle is not valid")
    else:
        print("This triangle is not valid")
else:
    print("This triangle is not valid")