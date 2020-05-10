n=int(input("write any natural no. his mindset:"))
our=1
sum_even=sum_odd=0
while our<=n:
    if our%2==0:
        sum_even+=our
    else:
        sum_odd+=our
    our+=1
print("sum of even integer =",sum_even)
print("sum of odd integer =",sum_odd)