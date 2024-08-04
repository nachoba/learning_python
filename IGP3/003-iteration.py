# Iteration
# =========
# A common idiom when dealing with sequences is to loop over the contents of
# the sequence.
# The 'for' loop is one way to do this:

letters = ['c', 'a', 't', 's']

for letter in letters:
    print(letter)

'''
c
a
t
s
'''

# During the execution of this loop, Python creates a new variable 'letter',
# that holds the item of iteration. 
# Note that te value of 'letter' is not the index position, but the string.
# This variable is not cleaned up by Python after the loop is done.

print("We are out of the loop")
print(f"The variable 'letter' holds {letter}")

'''
We are out of the loop
The variable 'letter' holds s
'''

# Occasionally you will also need the index position of the item. Python
# provides the buit-in 'enumerate' function that does that. This function
# returns a tuple of '(index, item)' for every item in the sequence:

animals = ["cat", "dog", "bird"]
for index, value in enumerate(animals):
    print(index, value)

'''
0 cat
1 dog
2 bird
'''

# You may need to stop processing a loop early, without going over every item
# in the loop. The 'break' keyword will jump out of the nearest loop you are in.
# We want to add numbers till a negative one appears

numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        break
    result += item

print(result)

'''
17
'''
# Another common looping idiom is to skip over items. The 'continue' statement
# tells Python to disregard processing of the current item in the for loop and
# contonue from the the top of the for block with the next value in the loop.
# In the following case we want to skip the negative numbers:

numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        continue
    result += item

print(result)

'''
21
'''

# The 'in' statement can be used to check membership. If you want to know if a
# list contains an item, you can use the 'in' statement to check that:

animals = ["cat", "dog", "bird"]
print('bird' in animals)

'''
True
'''

# If you want the index location, use the '.index()' method

print(animals.index('bird'))

'''
2
'''

# Summary
# =======
# You can define your own classes that respond to the 'for' statement, by
# implementing the '.__iter__' method.
# The for loop creates a variable during iteration, this variable is not gar-
# bage collected after the loop. If your for loop is inside of a function, the
# variable will be garbage collected when the function exits.

# The 'enumerate' function returns a sequence of tuples of (index, item) pairs
# for the sequence passed into it. If you need to get the index location as
# well as the item of iteration, use 'enumerate'.

# Exercises
# _________
# 1. Create a list with the names of friends and colleagues. Calculate the 
#    average length of the names.

names = ["Nacho", "Lucas", "Gabriel", "Facundo", "Pedro"]
letters = 0

for name in names:
    letters += len(name)

average = letters / len(names)
print(average)

# 2. Create a list with the names of friends and colleagues. Search for the name
#    'john' using a for loop. Print "not found" if you didn't find it.
#    (Hint: use 'else')
for name in names:
    if name == "John":
        print("John found")
        break
    else:
        print("Not found")

# 3. Create a list of tuples of first name, last name, and age for your friends.
#    If you don't know the age, put in 'None'. Calculate the average age, 
#    skipping over any 'None' values.
#    Print out each name, followed by "old" or "young" if they are above or
#    below the average age


       




