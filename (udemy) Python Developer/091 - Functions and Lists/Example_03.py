# You can take user inputs when calling a function.

# This code prompts for user input each time
# the function is called, adding the entered
# value to the list.

cart = []

def add_to_cart(cart):
    #taking user-input
    product = input()
    cart.append(product)
    
add_to_cart(cart)
print(cart)