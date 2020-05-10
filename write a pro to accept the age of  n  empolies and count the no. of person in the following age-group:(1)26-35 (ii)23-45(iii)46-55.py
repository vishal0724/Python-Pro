a=b=c=0
age=list(map(int,input().split()))
for i in age:
    if 25<i<=35:
        a+=1
    elif(35<i<=45):
        b+=1
    elif 45<i<=55:
        c+=1
    print(a,'in 26-35,',b,'in 36-45,',c,'in 46-55')