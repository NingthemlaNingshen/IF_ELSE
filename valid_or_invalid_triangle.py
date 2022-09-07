#triangle(valid or invalid)(equilateral,isoceles,or scalene)
num1=int(input("any number="))
num2=int(input("any number="))
num3=int(input("any number="))
if (num1+num2>num3 and num2+num3>num1 and num1+num3>num2):
    print("triangle is valid")
else:
    print("invalid")