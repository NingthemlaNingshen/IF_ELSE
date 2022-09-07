#find out the youngest to oldest

age1=int(input("enter the age="))
age2=int(input("enter the age="))
age3=int(input("enter the age="))
if(age1>age2 and age1>age3):
    print(age1,"older")
if(age2>age3 and age2>age1):
    print(age2,"older")
if(age3>age1 and age3>age2):
    print(age3,"older")
if(age1<age2 and age1<age3):

    print(age1,"younger")
if(age2<age3 and age2<age1):
    print(age2,"younger")
if(age3<age1 and age3<age2):
    print(age3,"younger")
else:
    print("equal age")