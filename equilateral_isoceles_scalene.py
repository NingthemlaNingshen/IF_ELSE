##equilateral/isoceles/scalene
num1=int(input("num="))
num2=int(input("num="))
num3=int(input("num="))
if(num1==num2 and num2==num3 and num3==num1):
    print("equilateral")
elif(num1==num2 or num2==num3 or num3==num1):
    print("isoceles")
else:
    print("scalene")



