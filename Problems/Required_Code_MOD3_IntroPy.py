"""
Program: Cheese Order

- set values for maximum and minimum order variables
- set value for price variable
- get order_amount input and cast to a number
- check order_amount and give message checking against
- over maximum
- under minimum
- else within maximum and minimum give message with calculated price

""" 

    max_amount = 100
    min_amount = 1
    price = 5

    order_amount = float(input("Enter cheese order weight (numeric value):"))

    if (order_amount > max_amount):
        print (order_amount, "is more than currently available stock")
    elif (min_amount <= order_amount <= max_amount):
        print (order_amount, "costs $", (price * (order_amount)))
    else:
        print (order_amount, "is below minimum order amount")
