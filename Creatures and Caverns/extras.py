import math
import random
import inspect
import sys


#HELPS SEPARATE THE DIALOGUE IN THE GAME
def separation():
    frame = inspect.currentframe().f_back
    prev_text = frame.f_locals.get('text', '')
    print(prev_text)
    if prev_text:
        print('-' * len(prev_text)) 

#SELF EXPLANATORY
def invalid_input():
    print("Invalid input.")

#HELPS WITH LUCK BASED ELEMENTS IN THE GAME
def roll(a,b):
    num = random.randint(a,b)
    return num   

#KILLSWITCH FOR THE REST OF THE CODE IF THE PLAYER DIES
def game_over():
    print('GAME OVER!')
    sys.exit()
