def grocery_menu():
    #to create a file and assign to a variable
    filename="grocery_list_2.txt"

    #Encoding for using special symbols
    with open(filename,"w",encoding='utf-8') as file:
        file.write("    ---the Grocery list---\n\n")

        #using while for get input from user infinitly
        while True:

            #to get the item name
            item=input("Enter item name, to exite leave empty line: ")
            
            #user enter empty line,the loop breaks
            if item == "":
                break
            
            #not allow the empty file
            if not item:
                print("List cannot be empty,please try again later")
                continue
            
            #using while for get input from user infinitly
            while True:
                #to get the quantity
                quantity=input('Enter quantity for the item: ')
                if not quantity.strip():
                    print("Do not give empty line")
                    continue
                #handling the errors using try and except blocks
                try:
                    quantity=int(quantity)
                    break
                except ValueError:
                    print("How much amount did you want?")


            while True:
                print("1-kg,2-g,3-mg,4-l,5-ml,6-pocket")
                p=input('Enter unit: ')
                try:
                    unit=int(p)
                    units=["kg","g","mg","l","ml","pocket"]
                    #using enumerate gives index while iterate
                    for i in enumerate(units,start=1): 
                        n=unit-1
                        selected_unit=units[n]
                    break
                except Exception:
                    print("Enter valid option for the unit!!")
            #It write the users input into the file
            file.write(f"➡️  {item} ---- {quantity}{selected_unit}\n")
#Run the programm            
grocery_menu()