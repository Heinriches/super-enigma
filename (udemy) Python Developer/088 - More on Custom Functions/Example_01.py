# A function can return multiple values.

# The function 'rect()' helps a real-state-agency
# to calculate the area and perimeter of a
# rectangular parcel of land. It takes the
# two-dimensions of the parcel as arguments.

def rect(length, width):
    area = (length * width)
    perimeter = ((2 * length) + (2 * width))
    return area, perimeter

x, y = rect(50, 100) # 2 variables
print(x, y)