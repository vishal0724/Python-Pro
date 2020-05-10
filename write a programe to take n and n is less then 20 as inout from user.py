n=int(input("enter any no.b/w (>20):"))
t=[]
for l in range(11,n+1):
    t.append (l)
print(t)
if n%3==0:
    print("tipsy")
elif n%7==0:
    print("Topsy")
else:
    n%3 or 7==0
    print("TipsyTopsy")