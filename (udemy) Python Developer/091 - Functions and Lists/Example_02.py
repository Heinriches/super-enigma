# Reusabilityis a key stregth of functions.
# The 'add_menu' function from the previous
# example can help you create a brand new menu
# from scratch. To do this, first you need
# to create an empty list.

#empty list
new_menu = []

#dishes for the new menu
dish1 = "Pasta"
dish2 = "Pizza"
dish3 = "Salad"

#function definition
def add_to_menu(menu, dish):
    menu.append(dish)

#adding dish 1
add_to_menu(new_menu, dish1)
print(new_menu)

#add dish 2
add_to_menu(new_menu, dish2)
print(new_menu)

#add dish 3
add_to_menu(new_menu, dish3)
print(new_menu)