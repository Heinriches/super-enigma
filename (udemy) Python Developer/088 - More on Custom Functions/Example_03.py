# Python allows function-arguments to have
# default-values. If the function is called
# without the argument, then the argument gets
# its default-value.

def greet(name = "Guest"):
    print("Welcome ", name)

greet() # Welcome Guest
greet("John") # Welcome John"