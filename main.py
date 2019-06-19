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

        #Base of feedback
        feedback = ['F'] * 4
        digits = [code.count(str(i)) for i in range(10)]
        count_digits = [i for i in digits]

        #Checks the user input against the secret code
        if guess == code:

            #If the user guessed the code in 1 turn
            if guess == code and guessesTaken == 1:
                print("Oof! You've beaten me in " + str(guessesTaken) +
                      " turn!")
                break

            #If the user guessed the code in more than 1 turn
            if guess == code and guessesTaken > 1:
                print("Oof! You've beaten me in " + str(guessesTaken) +
                      " turns!")
                break
        else:
            for i, digit in enumerate(guess):
                index = int(digit)
                if count_digits[index] > 0 and code[i] == digit:
                    count_digits[index] -= 1
                    feedback[i] = 'G'
                elif count_digits[index] > 0:
                    count_digits[index] -= 1
                    feedback[i] = 'C'

        #Checks whether the user inputted an Easteregg
        if guess != code and guess == e1 or guess == e2 or guess == e3 or guess == e4:

            #Easteregg nr. 1
            if guess == e1:
                print("Yeah! You've found the birthyear of BNT!")

            #Easteregg nr. 2
            elif guess == e2:
                print("Yeah! You've found the birthyear of LGG!")

            #Easteregg nr. 3
            elif guess == e3:
                print(
                    "Yeah! You've found the birthdate of one of the developers of this game, Woet!"
                )

            #Easteregg nr. 4
            elif guess == e4:
                print(
                    "Yeah! You've found the birthdate of one of the creators of this game, Robert!"
                )
            guessesTaken = guessesTaken - 1
        else:
            print(*feedback, sep=" ")


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
                "Do you want to play again (and be beaten this time)? (yes / no)"
            )

        #Input on whether the user wants to play again.
        play_again = input()

        #Restarts the game.
        while play_again.lower() != "no" or play_again.lower() != "yes":
            if play_again.lower() == "yes":
                print("Great choice! This time, it won't be so easy!")
                main()
                break

            #Stops the game
            elif play_again.lower() == "no":
                print(
                "That's too bad.... But hey, it was fun, and I hope to see you again soon, "
                + name + "!")
                exit()

            #Checks if the correct input has been given on whether the user wants to play again
            else:
                print("Please answer with either yes or no.")
                play_again = input()


play_again()
