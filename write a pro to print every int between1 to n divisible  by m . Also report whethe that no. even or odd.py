n=int(input("Enter the no. where we find int.:"))
m=int(input("enter the no. which divide the int.:"))
for i in range(1,n+1):
    if i%m==0:
        if i%2==0:
            print(i,'even')
        else:
            print(i,'odd')
