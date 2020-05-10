l=int(input('enter a list of no.:'))
for n in range(l):
    for i in range(len(n)/2):
        if n[i]!=n[-(i+1)]:
            break
else:
    print(n,"is a palindrome")]