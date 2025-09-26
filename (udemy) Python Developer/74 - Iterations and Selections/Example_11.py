# You can combine ranges and lists in nested-loops.
# This is a code-fragment from a dance-training-application:

moves = ["Step-Turn", "Jazz-Hands", "Shuffle"]

for move in moves:
    for i in range(3):
        print(move)