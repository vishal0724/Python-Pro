 
j,i=1,1
l=[]
while i<=40:
    if j%2!=0:
        l.append(i)
    else:
        l.append(-i)
    i+=3
    j+=1
print(l)