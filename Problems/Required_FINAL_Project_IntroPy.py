def adding_report(choice):
    total = 0
    i = 0
    items = ""
    user_input = ""
    while user_input.isalpha() == False:
        while True:
            user_input = input("Enter an integer or Q:")
            if user_input.isalpha() == True:
                if (user_input.lower() == "q") or (user_input.lower() == "Quit"):
                    user_input = input("Enter a vaild integer or enter Q: ")
                else:
                    break
            else:
                items = items + "\n" + user_input
                total = total + int(user_input)
                i = i + 1
    if choice == "A":
        print("Items\n", items) 
        print("Total\n", total) 
    elif choice=="T": 
        print("Total\n", total)
        
adding_report("A")
