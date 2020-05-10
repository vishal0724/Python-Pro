lst=[]
n=int(input("how many no. in list:"))
for i in range(0,n):
    ele=int(input("Enter the no.:"))
    lst.append(ele)
for t in (sorted(lst)):
    pass 
print("The largest no. in this series is ",t)