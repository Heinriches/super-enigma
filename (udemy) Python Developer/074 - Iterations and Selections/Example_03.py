# A loop can have another loop nested within it. This
# means that for each iteration of the outer (main)
# loop, the inner loop will run entirely.

# This nested loop will display all possible combinations
# of ranks and suits from the given lists:

ranks = ["Ace", "King", "Queen"]
suits = ["Hearts", "Clubs", "Diamonds"]

for rank in ranks:
    for suit in suits:
        print(rank, suit)
        
# Each iteration of the outer loop runs the inner loop
# entirely, with corresponding iterator values.