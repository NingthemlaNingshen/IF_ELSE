start=int(input("Janmansh started the assignments at: "))
last_date=int(input("Last date to submit the assignments: "))
assignments=3
if assignments+start<=last_date:
    print("he can completed the assignments.")
else:
    print("He can not complete all the 3 assignments ")