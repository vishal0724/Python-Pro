bill=int(input("Enter the electricity unit:"))

if (bill<=50):
    print("electricity bill=",bill*0.5)
elif(bill<=150):
    print("electricity bill=",(50*0.5)+(bill-50)*0.75)
elif(bill<=250):
    print("electricity bill=",((50*0.5)+(100*0.75))+(bill-150)*1.2)
else:
    print("electricity bill=",((50*0.5)+(100*0.75)+(100*1.2))+(bill-250)*1.5)