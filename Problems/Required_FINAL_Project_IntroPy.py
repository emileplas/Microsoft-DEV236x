"""
Program: adding_report() Function

This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".
The adding_report() function has 1 string parameter which indicates the type of report:
    -"A" used as the argument to adding_report() results in printing of all of the input integers and the total
    -"T" used as the argument results in printing only the total
    
Additional Details
    -initialize total variable which will sum integer values entered
    -initialize items variable which will build a string of the integer inputs separated with a new line character
    -define the adding_report function with one parameter report that will be a string with default of "T"
    -inside the function build a forever loop (infinite while loop) and inside the loop complete the following
    -use a variable to gather input (integer or "Q")
    -check if the input string is a digit (integer) and if it is...
    -add input iteger to total
    -if report type is "A" add the numeric character(s) to the item string seperated by a new line
    -if not a digit, check if the input string is "Q" or starts with a "Q", if "Q" then...
    -if the report type is "A" print out all the integer items entered and the sum total
    -if report type is "T" then print out the sum total only
    -break out of while loop to end the function after printing the report ("A" or "T")
    -if not a digit and if not a "Q" then print a message that the "input is invalid"
    
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
