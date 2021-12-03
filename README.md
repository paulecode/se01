# se01
Assessment for SE01

paul ebert 2021 dec 3

# Ex 4 theorycrafting:

Creating a tree of all next possible moves, iterating through them, if there is no possible solution, then the game ends.

For the winning condition, iterate through all beakers.

Converting them to sets then removes duplicates (they are equal to each other) Then checking the length <= 1 should tell us whether they are all empty or equal.

The loop probably doesn't work right now because I used `copy()`, and I probably won't find the source of this in the remaining time on top of fixing everything else
# Note

Exercise 3 contains an updated solution for exercise 2
