import random
print("You are in a dark room in a mysterious castle...")
print("...In front of you are five doors. You must choose one...")
doorchoice = input("...Choose 1, 2, 3, 4 or 5...")
if doorchoice == "1":
    print("You find a room filled with treasure! You win!")
elif doorchoice == "2":
    print("An angry ogre runs out and hits you with his club. You lose.")
elif doorchoice == "3":
    print("you find a room at floor level! You smash a window with a chair and climb out!")
elif doorchoice == "4":
    dragonchoice = input("you find a dragon, surrounded by treasure, guarding the exit. Do you try to: 1: sneak past the dragon or 2: steal some of it's gold? Answer 1 or 2 please.")
    if dragonchoice == "1":
        print("You manage to sneak past the dragon and emerge in the golden sunlight! You win!")
    elif dragonchoice == "2":
        print("you drop a gold coin and the dragon wakes up and engulfs you in flames. You lose.")
    else: print("You didn't enter 1 or 2.")
elif doorchoice == "5":
    print("You enter a room with a sphinx.")
    print("It asks you to guess what number it is thinking of, Between 1 and 10")
    sphinxchoice = int(input("what number do you choose? Answer 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 please"))
    if sphinxchoice == random.randint (1, 10):
                       print("The sphinx hisses in disappointment. You guessed correctly.")
                       print("She must let you go free. You win")
    else:
        print("The sphinx tells you your guess was incorrect.")
        print("You are now her prisoner forever. You lose")
else: print("You did not enter a valid number")
