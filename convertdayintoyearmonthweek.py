day=int(input("enter the no. of day:"))
year=day//365
month=(day-(year*365))//30
remaningDays=(day-(year*365)-(month*30))//7
print("year=:",year)
print("month=:",month)
print("week=:",remaningDays)
