Balance=int(input("enter the amount: "))
pin=int(input("enter your prefered pin:"))
print("Wlecome to State Bank Of India\nPlease Insert yor debit card\nSelect your language")
user1=input("Select language: ")
if user1=="English":
    print("Confirm your Identity by entering your Personal Identification Number ")
    user=input("Enter your PIN: ")
    if user==pin:
        print("Choose your option\nWithdraw\nDeposit\nMinistatement\nBalance Inquiry")
        User=input("enter what you want to do: ")
        if User=="Withdraw":
            Amount=int(input("Enter how much you want to withdraw: "))
            if Amount<Balance:
                print("Insufficient balance")
            else:
                print(Amount,"\nyour transaction is processed\nPlease wait\nPlease collect your cash\n Do you want to see your balance? ")
                ans=input(" ")
                if ans=="yes" or "Yes" or "y":
                    print("Remaining balance in your account:",Balance-Amount)
                else:
                    print("Hope you are satisfied with our service")
        elif User=="Deposit":
            print("Hi, Please do not remove your card.\nLeave your card inserted during the entire transation.")
            Amount=int("Enter the amount: ")
            print("Your Transaction is being processed\n Please wait..\n Transaction sucessful")
            print(Balance+Amount,"is in your account")
        elif User=="Balance Inquiry":
            print(Balance,"is in your account")
        else:
            print("Do you want to show it on screen")
            ans=input("")
            if ans=="yes":
                print("Available balance:",Balance)
            else:
                print("Please try saving paper by looking on the screen")
    else:
        print("The entered pin is incorrect")
else:
    print("Sorry other option is currently not available\n Sorry for the inconvinence")
