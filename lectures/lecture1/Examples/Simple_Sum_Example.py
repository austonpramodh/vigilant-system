# Retrive two numbers from the user and add them together. Display the result to the user

# Retrieving numbers
print("Enter the first number") # 'print': display the string to the user (via the console)
num1 = input() #'input': retrive input from the user (via the console)
print("Enter the second number")
num2 = input() 

# When input is gathered from the user, it is a string. We need to
# convert the string to a number ('int' or 'float') to perform arithmetic. Changing
# the type of a variable is called "Type Conversion"
num1 = int(num1)
num2 = int(num2)

# Adding two variables
sum = num1 + num2 

# When we display information to a user, we must use strings. Therefore we now need
# to convert our numbers to strings
num1 = str(num1)
num2 = str(num2)
sum = str(sum)

# Display the result of the addition
print("The sum of '" + num1 + "' and '" + num2 + " is '" + sum + "'")

# Note: 'num1', 'num2', and 'sum' are variables
# Note: '+' can be used to add numbers and join strings. Joining strings is called "concatenation"
# Note: Operator Overloading is when operators perform more than function, like '+' both adds numbers and joins strings


