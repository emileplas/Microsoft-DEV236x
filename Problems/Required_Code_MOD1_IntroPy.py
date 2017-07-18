"""
Program: Allergy Check

Uses input to check T/F within a list

"""

# [ ] get input for input_test variable

input_test = input("What all have you eaten in the last 24 hours?: ")

# [ ] print "True" message if "dairy" is in the input or False message if not

print ("Have eaten dairy: ", 'dairy'.lower() in input_test.lower())

# [ ] print True message if "nuts" is in the input or False if not

print ("Have eaten nuts: ", 'nuts'.lower() in input_test.lower())

# [ ] Challenge: Check if "seafood" is in the input - print message

print ("Have eaten seafood: ", 'seafood'.lower() in input_test.lower())

# [ ] Challenge: Check if "chocolate" is in the input - print message

print ("Have eaten chocolate: ", 'chocolate'.lower() in input_test.lower())

