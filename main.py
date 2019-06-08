# ---- Hack the pincode: the game -----
print("------ HACK THE PINCODE: THE GAME ------")


#chooses the random pincode that needs to be hacked

import random

pincode = [
    '1231' '9997', '8829', '6765', '9114', '5673', '0103', '4370', '8301','1022'
]
x = random.choice(pincode)
turns = 0

name = input("Hi there stranger! What do I call you? ")

print("Hi, " + name)

#asks whether the user wants a tutorial

tutorial = input("Do you want a tutorial? (yes / no)")

if tutorial == "yes":
  print("10 turns. 4 numbers. The goal? Hack the pincode.")
  print("For every number in the pincode you've come up with, I'll tell you whether it is correct AND correctly placed (G), correct but placed incorrectly (C) or just plain wrong (F).")
  guess = input("So now that that's out of the way, go ahead, and take your first guess!")
elif tutorial == "no":
  guess = input(name +
      ", I am thinking of a 4 number long pincode. Can you guess what it is?")
else:
    tutorial = input("Please answer with yes or no")


#checks whether the user pincode is the correct one

if guess == x:
  print("Hooray! You've beaten the game!")
  again = input("Do you want to play again? (yes / no)")
else:
  guess = input("Take another guess, " + name)