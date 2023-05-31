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