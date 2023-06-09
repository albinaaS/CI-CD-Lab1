import random
import time
import emoji
import argparse

action = "easy"

rock = emoji.emojize(":rock:")
paper = emoji.emojize(":page_facing_up:")
scissors = emoji.emojize(":scissors:")
lizard = emoji.emojize(":lizard:")
spock = emoji.emojize(":vulcan_salute:")

items = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "spock"}
emoji_items = {1: rock, 2: paper, 3: scissors, 4: lizard, 5: spock}
i = 0

def is_win(user_item,bot_item):

    if (user_item == 1 and bot_item in (3, 4)) or (user_item == 2 and bot_item in (1, 5)) or \
            (user_item == 3 and bot_item in (2, 4)) or (user_item == 4 and bot_item in (2, 5)) \
            or (user_item == 5 and bot_item in (1, 3)):
        return True
    return False

def win_mes(user_item,bot_item,mode="CPU"):

    if mode == "CPU":
        if is_win(user_item,bot_item):
            return "You WIN!"
        else:
            return "You LOSE!"
    elif mode == "Player":
        if is_win(user_item,bot_item):
            return "WIN of Player 1"
        else:
            return "WIN of Player 2"

def lose():
    return "YOU LOSE!"

def choise():
    global i
    if i == 0:
        print("1 - vs CPU\n2 - vs Player")
        i = int(input())
        while i != 1 and i != 2:
            print(f"Wrong, try again:")
            i = int(input())

def bot(user_item,bot_item):
    print("\nYou chose " + items[user_item])
    time.sleep(1)

    print("Computer chose " + items[bot_item] + "\n")
    time.sleep(0.5)
    game_core(bot_item, user_item)

def game_core(bot_item, user_item):

    print(emoji_items[user_item] + "\t" + emoji.emojize(":right_arrow:") + "\t" + emoji_items[bot_item])

    if user_item == bot_item:
        print("TIE! MOVE TO NEXT ROUND!")
        game()

    if i == 2:
        print(win_mes(user_item,bot_item,mode="Player"))
    else:
        print(win_mes(user_item, bot_item))

def player(user_item,bot_item):
    print("\nPlayer 1 " + items[user_item])
    time.sleep(0.5)

    print("Player 2 " + items[bot_item] + "\n")
    time.sleep(0.5)
    game_core(bot_item, user_item)

def selection(res:str,number:int):
    user_item = 0
    while user_item > number or user_item <= 0:
        user_item = int(input(res + "\n\tYour item: "))
    if i == 2:
        a = "\n" * 15
        print(f"{a}" + "Do not scroll up :)\n")
        bot_item = 0
        while bot_item > number or bot_item <= 0:
            bot_item = int(input(res + "\n\tYour item: "))
        player(user_item, bot_item)
    else:
        bot_item = random.randint(1, number)
        bot(user_item, bot_item)

def game():

    choise()

    res = ""
    number = 0
    if action == "easy":
        number = 3
        for a in range(3):
           print(f'\t{a+1} - {items[a+1]}. {items[a+1].title()} {emoji_items[a+1]}')

    elif action == "hard":
        number = 5
        res = '\n'.join(map(lambda item: f'\t{item[0]}. {item[1].title()} {emoji_items[item[0]]}', items.items()))
    selection(res,number)

    print("==============================================================================")
    if input("Do you want to start a new game? (y) ").lower() == "y":
        game()
    else:
        print("Awesome game! See you...")
        exit(0)

def say_hello():
    name = input("What is your first name?")
    print("Hello " + name)
    return "Hello " + name

if __name__ == "__main__":
    say_hello()
    try:
        with open("Greeting.txt") as file:
            print(file.read())
    except:
        pass

    start = str(input("Do you want to start the game? (y) "))

    if start.lower() == "y":
        game()
    else:
        print("\nOK, see you next time...Bye!")

