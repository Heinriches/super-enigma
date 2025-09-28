# MISTAKE REPETITION

# This code will display itens that DON'T start with 'l'.


animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
    if animal[0] == "l":
        continue
    print(animal)
    