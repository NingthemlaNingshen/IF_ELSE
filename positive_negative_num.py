#positive or negative
num1=int(input("enter the number="))
if num1>0:
    print("positive")
else:
    print("negative")

purchase_quantity=int(input("enter the purchase_quantity= "))
if purchase_quantity>1000:
    print("there will be discount of 10%=",purchase_quantity-(10*100/1000))
else:
    print("no discount")