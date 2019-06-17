# ---- Hack the pincode: the game -----
print("------ HACK THE PINCODE: THE GAME ------")

#chooses the random pincode that needs to be hacked
import random
pincode = [
    '1231', '9997', '8829', '6765', '9114', '5673', '0103', '4370', '8301',
    '1022'
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
            print(
                "For every number in the pincode you've come up with, I'll tell you whether it is correct AND correctly placed (G), correct but placed incorrectly (C) or just plain wrong (F)."
            )
            break

        #Skips tutorial
        elif tutorial.lower() == "no":
            break

        #Checks if the correct input has been given
        else:
            print("Please answer with either yes or no.")
            tutorial = input()


introduction()


#Main code for the game
def main():
    global code
    global guess

    #Chooses random pincode
    code = random.choice(pincode)

    #Sets guessestaken to 0
    guessesTaken = 0

    while guessesTaken < 10:

        #Makes sure every turn, an extra guess is added
        guessesTaken = guessesTaken + 1

        #Asks for user input
        print("This is turn " + str(guessesTaken) + ". Try a code!")
        guess = input()

        #Easteregg codes
        e1 = "1955"  #Birthyear of BNT
        e2 = "1980"  #Birthyear of LGG
        e3 = "1807"  #Birthdate of Woet
        e4 = "0609"  #Birthdate of Robert

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

            #In case the user guesses the code in 1 turn
            if (guessesTaken) == 1:
                print("Well done, " + name + "! You've hacked the code in " +
                      str(guessesTaken) + " turn!")

            #In cases the user guesses the code in more than 1 turn
            else:
                print("Well done, " + name + "! You've hacked the code in " +
                      str(guessesTaken) + " turns!")
            return

        #Sets empty list for the feedback on the user inputted code
        feedback = []
        nodouble = []

        #Iterates from 0 to 4
        for i in range(4):

            #Compares the items in the list to eachother
            if guess[i] == code[i]:

                #A match means the letter G is added to feedback
                feedback.append("G")
                nodouble.append(guess[i])

            #Checks if the guess number is contained in the code
            elif guess[i] in code:

                #Makes sure the position of the numbers isn't the same
                if guess[i] != code[i]:
                    if guess[i] not in nodouble:

                        #The letter is added to feedback[]  if there's a match
                        feedback.append("C")
                        nodouble.append(guess[i])

            #If the statements above are false, this is executed
            elif guess[i] not in code:

                #No match at all means an F is added to feedback[]
                feedback.append("F")
                nodouble.append(guess[i])

        #Easteregg
        if guess != code and guess == e1 or guess == e2 or guess == e3 or guess == e4:
            if guess == e1:
                print("Yeah! You've found the birthyear of BNT!")
            elif guess == e2:
                print("Yeah! You've found the birthyear of LGG!")
            elif guess == e3:
                print(
                    "Yeah! You've found the birthyear of one of the developers of this game, Woet!"
                )
            elif guess == e4:
                print(
                    "Yeah! You've found the birthdate of one of the creators of this game, Robert!"
                )
            guessesTaken = guessesTaken - 1
        else:
            print(*feedback, sep=' ')


main()


#The player has te option to play again
def play_again():
    while True:
        #In case the player lost the game
        if code != guess:
            print("Hahahahaha! You've lost! The correct code was " + code +
                  ". Do you want to try again, and win this time? (yes / no)")
        #In case the player won the game
        elif code == guess:
            print(
                "Oof. You've beaten me.... Do you want to be play again (and be beaten this time)? (yes / no)"
            )

        #Input on whether the user wants to play again.
        play_again = input()

        #Restarts the game.
        if play_again.lower() == "yes":
            print("Great choice! This time, it won't be so easy!")
            main()

        #Stops the game
        elif play_again.lower() == "no":
            print(
                "That's too bad.... I really enjoyed playing with you! But hey, it was fun, and I hope to see you again soon, "
                + name + "!")
            exit()

        #Checks if the correct input has been given on whether the user wants to play again
        else:
            print("Please answer with either yes or no.")
            play_again = input()


play_again()
