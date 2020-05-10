for num in range(15,25+1):
    for a in range (2,num//2):
        if num%a==0:
            break
    else:
       print("it is prime no.:",num)