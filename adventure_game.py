import time
import random
inventory = []


def random_person():  # you will meet either a wounded priestess or a girl
    random_woman = ["wounded priestess", "crying girl"]
    return random.choice(random_woman)


def print_pause(your_code):  # prints your code and after that a 2 sec pause
    print(your_code)
    time.sleep(2)


def new_game():  # lets you start a new game, after the game finishes
    answer = input("Do you want to play again?\n"
                   "yes\n"
                   "no\n")
    if "yes" in answer:
        complete_game()
    elif "no" in answer:
        print_pause("Ok Goodbye")
    else:
        print_pause("You must choose yes or no!")
        new_game()


def intro():  # the intro story for the game. starts every time the game starts
    print_pause("Finally, after many years, you found him.")
    print_pause("The man you once called your brother and mentor...")
    print_pause("You have been on the hunt for too long.")
    print_pause("Rumor has it, that Donovan and his bandits,\n"
                "your former friends, are around here, terorising\n"
                "the folk and looting the nearby temple!")
    print_pause("Your time for revenge has now come!")
    print_pause("Donovan's life is forfeit!")
    print_pause("You have positioned yourself on a mountain\n"
                "in front of the town.")
    print_pause("Watching what is in front of you...")
    print_pause("Only death and destruction...")
    print_pause("You look forward and see a town aflame, miles away")
    print_pause("A little bit west of the town you see\n"
                "the temple, also aflame")
    print_pause("In your hand is your crude sword,\n"
                "the Dragonslayer, a powerful but used sword.")


def choosing_path():  # lets you choose between town and temple
    choice = input("On the top of the montain, you need to decide,\n"
                   "which path you want to take.\n"
                   "Enter 1 to go to the town\n"
                   "Enter 2 to go to the ravaged temple\n")
    if choice == "1":
        town()
    elif choice == "2":
        temple()
    else:
        print_pause("You must choose a path, young warrior!")
        choosing_path()


def town():  # this happens the when you enter the town
    print_pause("You enter the town.")
    print_pause("After walking through streets full of dead civilians,\n"
                "you find him, cursed Donovan, leader of the bandits!")
    print_pause("It seems that he is alone. His men are too busy looting.")
    print_pause("This is your chance. You have waited\n"
                "so long for that moment!")
    while True:
        choice = input("What do you want to do?\n"
                       "Enter 1 to attack\n"
                       "Enter 2 to withdraw\n")
        if choice == "1":
            if "Obilisk" in inventory:
                print_pause("You attack, and with the power"
                            " of the Obilisk,"
                            " you enhance your sword and strike"
                            " down Donovan for good.")
                print_pause("You have won! Your lust for\n"
                            "revenge is satisfied.")
                print_pause("Now you can move on with your new life.")
                new_game()
                break
            else:
                print_pause("You attack, but your crude sword Dragonslayer\n"
                            "has no effect on Donovan's heavy armor!")
                print_pause("Whith an evil smile he strikes you down.")
                print_pause("You are dead!")
                print_pause("Game Over. You loose!")
                new_game()
            break
        elif choice == "2":
            print_pause("You decide to withdraw. Live today,"
                        " fight tomorrow!.")
            print_pause("You go back to your starting location.")
            choosing_path()
        else:
            print_pause("You must choose! Fight or withdraw!")


def temple():  # ths happens when you enter the temple.
    print_pause("You go to the ravaged temple.")
    if "Obilisk" in inventory:
        print_pause("The person who gave you the Obilisk is not here anymore.")
        print_pause("You go back to the mountain.")
        choosing_path()
    else:
        print_pause(f"In the temple, you find a {random_person()}.")
        print_pause("She gives you an Obilisk, a mighty artifact.")
        print_pause("\"You are going to need it\", she whispers.")
        print_pause("(Obilisk added to Inventory)")
        inventory.append("Obilisk")
        print_pause("You go back to the mountain")
        choosing_path()


def complete_game():  # all functions combined in this function. The whole game
    intro()
    choosing_path()


complete_game()
