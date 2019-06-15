# ---- Hack the pincode: the game -----
print("------ HACK THE PINCODE: THE GAME ------")


#chooses the random pincode that needs to be hacked
import random
pincode = [
  "1231", #'9997', '8829', '6765', '9114', '5673', '0103', '4370', '8301','1022'
]
code = random.choice(pincode)

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


  guessesTaken = 0
  while guessesTaken < 10:
    guessesTaken = guessesTaken + 1
    print("This is turn " + str(guessesTaken) + ". Try a code!")
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

    print(codeList)
    print(guessList)

    feedback = ""
    print(feedback)

    if codeList[0] == guessList[0]:
      print("G")
    elif codeList[0] == guessList[0:4]:
      print("C")
    else:
      print("F")
    
    if codeList[1] == guessList[1]:
      print("G")
    elif codeList[1] == guessList[0:4]:
      print("C")
    else:
      print("F")

    if codeList[2] == guessList[2]:
      print("G")
    elif codeList[2] == guessList[0:4]:
      print("C")
    else:
      print("F")

    if codeList[3] == guessList[3]:
      print("G")
    elif codeList[3] == guessList[0:4]:
      print("C")
    else:
      print("F")    
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
  nicknames = [
  "Mate", "Friend", "Buddy", "Son", "Niffauw", "Fella", "Bro", "", ""
  ]
  nickname = random.choice(nicknames)
  while True:
    #Restarts the game
    print("That sure was a great game, " + nickname.lower() + ". Do you want to play again? (yes / no)")
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