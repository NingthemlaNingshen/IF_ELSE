#leap year
year=int(input("enter the year="))
if year%4==0 and year%400==0:
    print("leap year")
elif year%100==0:
    print("century")
else:
    print("normal year")

# or
year=int(input("year="))
if ((year%400==0)or (year%4==0)) and ((year%100!=0)):
    print("leap year")
else:
    print("not leap year")