list1=[]
num=int(input("How many no.:"))
for i in range(1,num+1):
    bravo=(input("Enter the no.:"))
    list1.append(bravo)
print("The second largest no. in this series is",sorted(list1)[-2])
