item=int(input("Enter the no. of buying items:"))
if item<10:
    print("The total cost which you must pay is",item*120)
elif item<100:
    print("The total cost which you must pay is",item*100)
else :    
    print("The total cost which you must pay is",item*70)
