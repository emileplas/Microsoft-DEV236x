"""
Program: str_analysis() Function

Create the str_analysis() function that takes 1 string argument and returns a string message.
The message will be an analysis of a test string that is passed as an argument to str_analysis().
The function should respond with messages such as:
    -"big number"
    -"small number"
    -"all alphabetic"
    -"multiple character types"

The program will call str_analysis() with a string argument from input collected within a while loop. 
The while loop will test if input is empty (an empty string "") and continue to loop and gather input until the user submits at least 1 character (input cannot be empty).
The program then calls the str_analysis() function and prints the return message.

"""

user_input = input("enter word or integer: ")

while user_input == "":
    user_input = input("enter word or integer: ")
def str_analysis():
    if user_input.isdigit() == True:
        if int(user_input) > 99:
            print(user_input, "is a pretty big number")
        else:
            print(user_input, "is a smaller number than expected")
    elif user_input.isalpha() == True:
        print (user_input, "is all alphabetical characters!")
        
str_analysis()
