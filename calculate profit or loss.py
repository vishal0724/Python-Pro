cp=int(input("Enter your c.p rs:"))
sp=int(input("Enter your s.p rs:"))
profit=(sp-cp)
loss=(cp-sp)
if (sp>cp):
    print("Profit on your rs:",profit)
else:
    print("loss on your rs:",loss)