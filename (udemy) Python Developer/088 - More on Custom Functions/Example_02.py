# It's up to you as a coder to define
# what operations happen inside your function.
# This then controls which data types can
# be handled and returned.

# The 'profitable()' function below determines
# whether buying a parcel of land is a good
# investment for a real-state-agency in
# a particular location.

def profitable(d1, d2):
    area = (d1 * d2)
    invest = (area > 700)
    return invest

buy = profitable(90, 120)

print(buy)