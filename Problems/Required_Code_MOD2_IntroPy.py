"""
Program: fishstore()

- fishstore() takes 2 string arguments: fish & price
- fishstore returns a string in sentence form
- gather input for fish_entry and price_entry to use in calling fishstore()
- print the return value of fishstore()

"""

fish_entry = input("What fish do you want?:")
price_entry = input("How much?:")

def fishstore(fish, price):
    return("Fish Type: " + fish.capitalize() + " costs $" + price)
    
print (fishstore(fish_entry, price_entry))
