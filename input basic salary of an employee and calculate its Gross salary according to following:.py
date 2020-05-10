salary=int(input("Enter your basic salary:"))
if (salary<=10000):
    print("Your gross salary is",salary+((salary/100)*20)+((salary/100)*80))
elif(salary<=20000):
    print("Your gross salary is",salary+((salary/100)*25)+((salary/100)*90))
else:
    print("Your gross salary is",salary+((salary/100)*30)+((salary/100)*95))
