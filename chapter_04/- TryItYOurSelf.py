# -*- coding: utf-8 -*-
# =============================================================================
# 4-1: Pizzas
# Think of at least three kinds of your favorite pizza. Store these pizza names
#  in a list, and then use a for loop to print the name of each pizza.

# Modify your for loop to print a sentence using the name of the pizza instead 
# of printing just the name of the pizza. For each pizza you should have one 
# line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how 
# much you like pizza. The output should consist of three or more lines about 
# the kinds of pizza you like and then an additional sentence, such as I really
#  love pizza!
# =============================================================================

# favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# # Print the names of all the pizzas.
# for pizza in favorite_pizzas:
#     print(pizza)

# print("\n")

# # Print a sentence about each pizza.
# for pizza in favorite_pizzas:
#     print(f"I really love {pizza} pizza!")

# print("\nI really love pizza!")




# =============================================================================
# 4-3: Counting to Twenty
# Use a for loop to print the numbers from 1 to 20, inclusive.
# =============================================================================

# numbers = list(range(1, 21))

# for number in numbers:
#     print(number)



# =============================================================================
# 4-5: Summing a Million
# Make a list of the numbers from one to one million, and then use min() 
# and max() to make sure your list actually starts at one and ends at one
#  million. Also, use the sum() function to see how quickly Python can 
#  add a million numbers.
# =============================================================================
# numbers = list(range(1, 1_000_001))

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))


# =============================================================================
# 4-7: Threes
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print 
# the numbers in your list.
# =============================================================================

# threes = list(range(3, 31, 3))

# for number in threes:
#     print(number)


# 4-8: Cubes
# A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first
#  10 cubes (that is, the cube of each integer from 1 through 10),
#  and use a for loop to print out the value of each cube.

# cubes = []
# for number in range(1, 11):
#     cube = number**3
#     cubes.append(cube)

# for cube in cubes:
#     print(cube)



# 4-9: Cube Comprehension
# Use a list comprehension to generate a list of the first 10 cubes.


# cubes = [number**3 for number in range(1,11)]

# for cube in cubes:
#     print(cube)



# 4-11: My Pizzas, Your Pizzas
# Start with your program from Exercise 4-1 (page 60). 
# Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:

# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message,
#  My favorite pizzas are:, and then use a for loop to print the first list.
#  Print the message, My friend’s favorite pizzas are:, and then 
#  use a for loop to print the second list. Make sure each new pizza 
#  is stored in the appropriate list.

# favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
# friend_pizzas = favorite_pizzas[:]

# favorite_pizzas.append("meat lover's")
# friend_pizzas.append('pesto')

# print("My favorite pizzas are:")
# for pizza in favorite_pizzas:
#     print(f"- {pizza}")

# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(f"- {pizza}")



# =============================================================================
# 4-13: Buffet
# A buffet-style restaurant offers only five basic foods. 
# Think of five simple foods, and store them in a tuple.
# 
# Use a for loop to print each food the restaurant offers.

# Try to modify one of the items, and make sure that Python rejects the change

# The restaurant changes its menu, replacing two of the items with
#  different foods. Add a block of code that rewrites the tuple, and
#  then use a for loop to print each of the items on the revised menu.
# =============================================================================

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item}")








