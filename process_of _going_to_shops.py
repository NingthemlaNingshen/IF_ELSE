Stationary_shopping_list="1. pen\n2. A4 size paper\n3. scissor\n4. marker\n5. colour\n6. pencil\n7. box\n8. book"
Greengrocer_shopping_list="1. pea\n2. Garlic\n3. onion\n4. carrot\n5. cabbage\n6. spinach\n7. cucumber\n8. mushroom"
Clothing_shopping_list="1. bedsheet\n2. towel\n3. curtain\n4. table_cloth\n5. shirt\n6. dress\n7. hat\n8. rainboots"
user=input("enter whether you want to go shopping or not? ")
if user=="No" or user=="no":
    print("Ok then let's Go when you are in mood.")
else:
    if user=="Yes" or user=="yes":
        print("Ok then are you prepared with your shopping lists? ")
        User=input("Answer in y or n: \n")
        if User=="n":
            print("Prepare a shopping list")
        else:
            shopping_place=input("Where are you going to do your shopping?")
            if shopping_place=="Stationary":
                print("Stationary_shopping_list\n",Stationary_shopping_list)
            elif shopping_place=="Greengrocer":
                print("Greengrocer_shopping_list\n",Greengrocer_shopping_list)
            elif shopping_place=="Clothing":
                print("Clothing_shopping_list\n",Clothing_shopping_list)
        print("Have a great time shopping")



