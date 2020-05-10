deposits=int(input("Enter your deposits amount in bank:"))
t=int(input("Enter the no. of years:"))
if ((deposits<2000) and (1<t)):
    print("Your amount  after specified time:",(deposits*(1+(5/100))**t))
elif ((deposits<6000) and (1<t)):
    print("Your amount  after specified time:",(deposits*(1+(7/100))**t))
elif ((deposits>6000) and (0<t)) :
    print("Your amount  after specified time:",(deposits*(1+(8/100))**t))
elif ((deposits>0) and (t>4)):
    print("Your amount  after specified time:",(deposits*(1+(8/100))**t))
else:
    print ("'So Sorry' but i'm not find compond intrest of this number.")