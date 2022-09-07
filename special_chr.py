#special charecter or alphabet
ch=input("any=")
if (ord(ch)>=65 and ord(ch)<=90)or(ord(ch)>=97 and ord(ch)<=122):
    print(ch, "is an alphabet")
else:
    print(ch, "is not alphabet")