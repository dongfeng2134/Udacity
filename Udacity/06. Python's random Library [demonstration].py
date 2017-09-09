# Python's `random` Library

# `random` is a Python "module". It provides functionality associated
# with randomness / probability. For now you don't need to know exactly
# what is happening when we write `import random as rd`, instead focus 
# on how we USE this module.
import random as rd

# Call the FUNCTION named random 3 times and assign the result of each
# call to a variable.
a = rd.random()
b = rd.random()
c = rd.random()
print("a is", a)
print("b is", b)
print("c is", c)

# random isn't the only function in the random module.
# Do a google search for "python random library" or 
# go here: https://docs.python.org/3/library/random.html
# to learn more.

print("Now keep pressing Ctrl+Enter to run this cell many times!")
print("Notice how the values of a,b, and c keep changing!")
