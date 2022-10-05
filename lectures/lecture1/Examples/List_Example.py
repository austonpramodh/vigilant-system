list_of_colors = ["red", "blue", "green"]
print(list_of_colors)

# Add a color to the list
list_of_colors.append("yellow")
print(list_of_colors)

# Get the first item in the list ("red") and store it to the variable "first_color"
# Note: This does not remove the item from the list
first_color = list_of_colors[0]
print("The first color in the list is " + first_color)

# Get the length of the list
number_of_colors = len(list_of_colors)
print("The number of items in the list is " + str(number_of_colors))

# Get and store the last item in the list
last_color = list_of_colors[number_of_colors - 1]
print("The last item in the list is " + last_color)

# Remove the color "blue"
list_of_colors.remove("blue")
print(list_of_colors)