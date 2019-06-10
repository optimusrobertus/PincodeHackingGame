# ---- Hack the pincode: the game -----
print("------ HACK THE PINCODE: THE GAME ------")


#chooses the random pincode that needs to be hacked

import random

pincode = [
    '1231', # '9997', '8829', '6765', '9114', '5673', '0103', '4370', '8301','1022'
]
code = random.choice(pincode)
guessesTaken = 0

print("Hi there stranger! What do I call you? ")
name = input()

print("Hi, " + name)

#Asks whether the user wants a tutorial

print("Do you want a tutorial? (yes / no)")
tutorial = input()

while tutorial.lower() != "no" or tutorial.lower() != "yes":
  if tutorial.lower() == "yes":
    print("10 turns. 4 numbers. The goal? Hack the pincode.")
    print("For every number in the pincode you've come up with, I'll tell you whether it is correct AND correctly placed (G), correct but placed incorrectly (C) or just plain wrong (F).")
    break
  elif tutorial.lower() == "no":
    break
  else:
    print("Please answer with either yes or no.")
    tutorial = input()


