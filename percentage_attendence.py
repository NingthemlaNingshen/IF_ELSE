#attendence,percentage
a=int(input("no. of calss held="))
b=int(input("no. of class attended="))
percentage=b/a*100
if (percentage>=75):
    print(percentage,"can attend exam")
else: 
    print(percentage,"can't attend exam ")