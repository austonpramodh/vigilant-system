my_dictionary = {"name": "Danielle", "age": 30, "favorite_color": "pink"}
print(my_dictionary)

# Add a key value pair to the dictionary
my_dictionary["does_like_dogs"] = True
print(my_dictionary)

# Get the value of the key "name" in the dictionary and store it to the variable "my_name"
# Note: This does not remove the item from the dictionary
my_name = my_dictionary['name']
print("My name is " + my_name)

# Get the number of items in the dictionary
length = len(my_dictionary)
print("The number of items in the list is " + str(length))

# Change the value of "age" to 25
last_color = my_dictionary["age"] = 25
print(my_dictionary)

# Remove the key value pair whose key is "favorite_color"
del my_dictionary["favorite_color"]
print(my_dictionary)