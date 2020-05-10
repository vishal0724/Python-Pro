a=float(input("Enter the temperature in celsius:"))
if a<-273.15:
    print('Temperature is invalid.')
elif a==-273.15:
    print("temperature is absolute 0.")
elif a<0:
    print('Temperature is below freezing.')
elif a==0:
    print('Temperature is at freezing point.')
elif a<100:
    print('Temperature is in normal range.')
elif a==100:
    print('Temperature is at boilling point.')
else:
    print('Temperature is above at bolling point.')