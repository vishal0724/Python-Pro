a=float(input("Enter the first no.:(this no. is also big than secont)"))
b=float(input("Enter the second no.:"))
if ((a-b)==.001) :
    print("close")
elif(b-a)==.001:
    print("close")
else:
    print("Not close")