a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
c=int(input("Enter the third no.:"))
if a > b:
    if b > c:
        ans = [a, b, c] 
    elif c > a:
        ans = [c, a, b] 
    else:
        ans = [a, c, b] 
else:
    if a > c:
        ans = [b, a, c] 
    elif c > b:
        ans = [c, b, a] 
    else:
        ans = [b, c, a] 
print("smallest number", ans[2])
print("Next Highest number", ans[1])
print("Highest number", ans[0])