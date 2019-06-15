# ---- Hack the pincode: the game -----
print("------ HACK THE PINCODE: THE GAME ------")


#chooses the random pincode that needs to be hacked
import random
pincode = [
  '1231', '9997', '8829', '6765', '9114', '5673', '0103', '4370', '8301','1022'
]

name = None

#Introduction to the game

def introduction():
  global name
  print("Hi there stranger! What do I call you? ")
  name = input()
  print("Hi, " + name)

  #Asks for tutorial
  print("Do you want a tutorial? (yes / no)")
  tutorial = input()

  #While loop for giving the tutorial
  while tutorial.lower() != "no" or tutorial.lower() != "yes":
    #Gives tutorial
    if tutorial.lower() == "yes":
      print("10 turns. 4 numbers. The goal? Hack the pincode.")
      print("For every number in the pincode you've come up with, I'll tell you whether it is correct AND correctly placed (G), correct but placed incorrectly (C) or just plain wrong (F).")
      break

    #Skips tutorial
    elif tutorial.lower() == "no":
      break

    #Checks if the correct input has been given
    else:
      print("Please answer with either yes or no.")
      tutorial = input()

introduction()

#The code given by the user is checked

def main():

  global code
  global guess

  code = random.choice(pincode)
  print(code)
  guessesTaken = 0
  while guessesTaken < 10:
    guessesTaken = guessesTaken + 1
    print("This is turn " + str(guessesTaken) + ". Try a code!")
    global guess

    guess = input()

    #Checks if only numbers have been inputted
    if guess.isdigit() == False:
      print("You can only use numbers, remember?")
      guessesTaken = guessesTaken - 1
      continue



    #Checks whether guess is 4 numbers long
    if len(guess) != len(code):
      print("The code is only 4 numbers long! Try again!")
      guessesTaken = guessesTaken - 1
      continue



    #Checks the code
    if guess == code:
      if (guessesTaken) == 1:
        print("Well done, " + name + "! You've hacked the code in " + str(guessesTaken) +" turn!")
      else:
        print("Well done, " + name + "! You've hacked the code in " + str(guessesTaken) +" turns!")
      return

    list(code)
    codeList = list(code)
    list(guess)
    guessList = list(guess)

    feedback = []


    if codeList[0] == guessList[0]:
      feedback.append("G")
    elif codeList[0] != guessList[0] and codeList[0] == guessList[1] or codeList[0] == guessList[2] or codeList[0] == guessList[3]:
      feedback.append("C")
    else:
      feedback.append("F")

    if codeList[1] == guessList[1]:
      feedback.append("G")
    elif codeList[1] != guessList[1] and codeList[1] == guessList[0] or codeList[1] == guessList[2] or codeList[1] == guessList[3]:
      feedback.append("C")
    else:
      feedback.append("F")

    if codeList[2] == guessList[2]:
      feedback.append("G")
    elif codeList[2] != guessList[2] and codeList[2] == guessList[0] or codeList[2] == guessList[1] or codeList[2] == guessList[3]:
      feedback.append("C")
    else:
      feedback.append("F")

    if codeList[3] == guessList[3]:
      feedback.append("G")
    elif codeList[3] != guessList[3] and codeList[3] == guessList[0] or codeList[3] == guessList[1] or codeList[3] == guessList[2]:
      feedback.append("C")
    else:
      feedback.append("F")

    print(*feedback, sep=' ')
    #else:

    #  for idx in range(0,3):
    #    guessNum = guess[idx]
    #    codeNum = code[idx]
    #  list(code)
    #  codeList = list(code)
    #  list(guess)
    #  guessList = list(guess)
main()

#The player has te option to play again

def play_again():
  while True:
    #Restarts the game
    if code != guess:
      print("You've lost! The correct code was " + code + ". Do you want to try again, and win this time?")
    elif code == guess:
      print("Oof. You've beaten me.... Do you want to be play again (and be beaten this time)? (yes / no)")
    play_again = input()
    if play_again.lower() == "yes":
      print("Great choice! This time, it won't be so easy!")
      main()

    #Stops the game
    elif play_again.lower() == "no":
      print("That's too bad.... I really enjoyed playing with you! But hey, it was fun, and I hope to see you again soon, " + name + "!")
      exit()

    #Checks if the correct input has been given
    else:
      print("Please answer with either yes or no.")
      play_again = input()

play_again()
