#Ex 4 theorycrafting:

Creating a tree of all next possible moves,
iterating through them, if there is no possible solution, then the game ends.

For the winning condition, iterate through all beakers.

Converting them to sets then removes duplicates (they are equal to each other)
Then checking the length <= 1 should tell us whether they are all empty or equal.