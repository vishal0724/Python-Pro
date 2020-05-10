ch=input ("Enter any character:")
if ((ch>='a' and ch <='z') or(ch>='A' and ch <='Z')):
    print("That character is an alphabet.")
elif((ch>='0'and ch <='9')or(ch>='0' and ch <='9')):
    print("That character is an digit.")
else:
    print("That character is an special character.")