# ---- Hack the pincode: the game -----
print("------ HACK THE PINCODE: THE GAME ------")


#chooses the random pincode that needs to be hacked
import random
pincode = [
  "1231", # '9997', '8829', '6765', '9114', '5673', '0103', '4370', '8301','1022'
]
code = random.choice(pincode)


#Introduction to the game

def introduction():
  print("Hi there stranger! What do I call you? ")
  name = input()
  print("Hi, " + name)
  print("Do you want a tutorial? (yes / no)")
  tutorial = input()
  
  #While loop for giving the tutorial
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

introduction()

#The code given by the user is checked

def main():
  guessesTaken = 0
  while guessesTaken < 10:
    guessesTaken = guessesTaken + 1
    print("Take a guess")
    guess = input()

    if guess == code:
      print("Well done, " + name.introduction() +"! You've hacked the code in " + str(guessesTaken) +" turns!")   
      break

main()


#The player has te option to play again

def play_again():
  nicknames = [
  "Mate", "Friend", "Buddy", "Son", "Cuz", "", "", "", ""
  ]
  nickname = random.choice(nicknames)
  while True:
    print("That sure was a great game, " + nickname + ". Do you want to play again? (yes / no )")
    play_again = input()
    if play_again.lower() == "yes":
      print("Great choice! This time, it won't be so easy!")
      main()
    elif play_again.lower() == "no":
      #print("That's too bad.... I really enjoyed playing with you! But hey, it was fun, and I hope to see you again soon, " + introduction(name) + "!")
      exit()
    else:
      print("Please answer with either yes or no.")
      play_again = input()

play_again()