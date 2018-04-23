#Countdown from 5
for countdown in (5,4,3,2,1,"Hey"):
    print(countdown)
for countdown in range (5,-1,-1):
    print(countdown)

#Emulating Numeric Types
import matplotlib.pyplot as plt
plt.plot([0,1,2,3,4],[0,1,4,9,16])
plt.show()

#Problems from the Introducing Python bookself.
# Booleans: syntax with a true or false value
# Interger: whole numbers (any number you can think of that has no decimals)
# Floats: numbers with decimal points
# Variables: names that refer to actual data [I want to understand variable in terms of computer science rather a component used to measure a change.]
# Strings: sequences of text characters - [still a bit confused on this and may need a bit of clarifiction]
#   These are simple built in data types that are similar to atoms. When we combine them, they create a molecule - or a working structureself.
#           Simple program to allow for staged changes
cliches = [
    "At the end of the day",
    "Having said that",
    "The fact of the matter is",
    "Be that as it may",
    "The bottom line is",
    "If you will",
    ]
print(cliches[3])
