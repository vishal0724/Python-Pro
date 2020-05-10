amount=float(input("enter your own amount:"))
amount1=((amount//2000)*2000)
amount2=((amount-(amount//2000)*2000)//500)*500
amount3=((amount-(((amount//2000)*2000 )+ ((amount-(amount//2000)*2000)//500)*500))//200)*200
amount4=((amount-(amount1+amount2+amount3))//100)*100
amount5=((amount-(amount1+amount2+amount3+amount4))//50)*50
amount6=((amount-(amount1+amount2+amount3+amount4+amount5))//20)*20
amount7=((amount-(amount1+amount2+amount3+amount4+amount5+amount6))//10)*10
amount8=((amount-(amount1+amount2+amount3+amount4+amount5+amount6+amount7))//5)*5
amount9=((amount-(amount1+amount2+amount3+amount4+amount5+amount6+amount7+amount8))//2)*2

print("No. of 2000 nots are:",amount//2000)
print("No. of 500 nots are:",(amount-(amount//2000)*2000)//500)
print("No. of 200 nots are:",(amount-(((amount//2000)*2000 )+ ((amount-(amount//2000)*2000)//500)*500))//200)
print("No. of 100 nots are:",(amount-(amount1+amount2+amount3))//100)
print("No. of 50 nots are:",(amount-(amount1+amount2+amount3+amount4))//50)
print("No. of 20 nots are:",(amount-(amount1+amount2+amount3+amount4+amount5))//20)
print("No. of 10 nots are:",(amount-(amount1+amount2+amount3+amount4+amount5+amount6))//10)
print("No. of 5 nots/coin are:",(amount-(amount1+amount2+amount3+amount4+amount5+amount6+amount7))//5)
print("No. of 2 coin are:",(amount-(amount1+amount2+amount3+amount4+amount5+amount6+amount7+amount8))//2)
print("No. of 1 coin are:",(amount-(amount1+amount2+amount3+amount4+amount5+amount6+amount7+amount8+amount9))//1)
