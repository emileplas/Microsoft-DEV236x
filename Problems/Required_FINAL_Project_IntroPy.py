"""
Program: adding_report() Function

This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".
The adding_report() function has 1 string parameter which indicates the type of report:
    -"A" used as the argument to adding_report() results in printing of all of the input integers and the total
    -"T" used as the argument results in printing only the total
    
"""

def adding_report(choice):
    total = 0
    i = 0
    items = ""
    user_input = ""
    while (user_input.upper() != "Q") or (user_input.upper().startswith("Q") != True) or (user_input.isdigit() == False):
        user_input = input("Enter an integer or 'Q': ")
        if (user_input.lower() == "q") or (user_input.lower().startswith("q") == True):
            break
        else:
            items = items + "\n" + user_input
            total = total + int(user_input)
            i = i + 1
            
    if choice == "A":
        print("Items\n", items) 
        print("Total\n", total) 
    elif choice == "T": 
        print("Total\n", total)

adding_report("T")
