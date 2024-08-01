# More About Object
# =================
#
# Three important topics to cover:
#
# + identity
# + type
# + value
#
# Identity
# --------
# Refers to an object's location in the computer's memory. Python has a built-in
# function called 'id' that tells the identity of an object:

name = "Nacho"
print(f"The identity of object name, which holds the string {name} is {id(name)}")


# It is possible for two variables to refer to the same object.
first = name

print("First object  ID", id(name))
print("Second object ID", id(first))

# Identity is used to illustrate when object are created and if they are mutable.
# It is also used indirectly for doing identity checks with 'is'

print("first is the same object as name?", first is name)

# Type
# ----
# Common types are: integers, floats, strings and booleans.
# The type of an object refers to the class of an object.
# A class defines the state of data an object holds, and the methods or actions that
# it can perform.
# Python allows you to easily view the type of an object with 'type(name)'
print(type(name))

# Python has built-in classes: str, int, float, dic, tuple that convert (or coerce)
# to the appropriate type if needed:
print(str(1))

# Mutability
# ----------
# Mutable objects can change their value in place: can alter their state, but their
# identity stays the same.
# Objects that are immutable do not allow you to change their value. Instead, you
# can change their variable reference to a new object, but this will change the
# identity of the variable as well.

# Dictionaries and lists are mutable types. 
# Strings, tuples, integers and floats are immutable types.
print("Immutable")
age = 100
print(id(age))

age = age + 1
print(id(age))

print("Mutable")
names = []
print(id(names))
names.append("Fred")
print(id(names))


# Summary
# -------
# + A Type indicates what the class is for the object.
# + A Value is the data that the object holds. When you test if an object is
#   equal to another object (with ==), you are checking against a value.
# + An ID is unique for the object. It is essentially the location in memory. You
#   check whether two objects have the same identity with 'is'.
# + Objects can be mutable or immutable.
#
# IS: 01/08/24
