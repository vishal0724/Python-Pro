print("convert centimeter into inch.")
cbi=float(input("Enter the length in centimeter:"))
if cbi<0:
    print("That is a invalid")
else :
    lot=cbi/2.54
    print("The result of this centimeter leanth into inch is",lot)
    pi=cbi*0.393701
print ("the difference between",lot,"and",pi, "is",pi-lot)