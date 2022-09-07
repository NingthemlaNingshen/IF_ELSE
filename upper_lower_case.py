#upper case or lower case
ch=input("any")
if(ord(ch)>=65 and ord(ch)<=90):
    print(ch,"upper case")
elif(ord(ch)>=97 and ord(ch)<=122):
    print(ch,"lower case")
else:
    print("not alphabet")