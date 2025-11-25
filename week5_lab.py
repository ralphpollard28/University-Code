"""""
# WET Code Block - Hard to read!
print("You are in a dark forest. You see two paths.")
choice1 = input("Do you go 'left' or 'right'? ")
if choice1 == 'left':
    print("You walk down the left path and find a river.")
    choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
    if choice2 == 'swim':
        print("You are tired from swimming and rest. You win!")
    elif choice2 == 'follow':
        print("You follow the river bank and find a hidden cave. You win!")
    else:
        print("Invalid choice. You are lost.")

elif choice1 == 'right':
     print("You walk down the right path and encounter a sleeping bear.")
     choice2 = input("Do you 'tiptoe' past or 'run' away? ")
     if choice2 == 'tiptoe':
         print("You successfully tiptoe past the bear and find a treasure chest. You win!")
     elif choice2 == 'run':
         print("You run away safely but get lost in the forest. Game over.")
     else:
         print("Invalid choice. You are lost.")
"""
"""
# DRY Code Block - Improved readability!
def start_scene():
    print("You are in a dark forest. You see two paths.")
    choice1 = input("Do you go 'left' or 'right'? ")
    if choice1 == 'left':
        left_path()
    elif choice1 == 'right':
        right_path()
    else:
        print("Invalid choice. You are lost.")

def left_path():
    print("You walk down the left path and find a river.")
    choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
    if choice2 == 'swim':
        print("You are tired from swimming and rest. You win!")
    elif choice2 == 'follow':
        print("You follow the river bank and find a hidden cave. You win!")
    else:
        print("Invalid choice. You are lost.")

def right_path():
    print("You walk down the right path and encounter a sleeping bear.")
    choice2 = input("Do you 'tiptoe' past or 'run' away? ")
    if choice2 == 'tiptoe':
        print("You successfully tiptoe past the bear and find a treasure chest. You win!")
    elif choice2 == 'run':
        print("You run away safely but get lost in the forest. Game over.")
    else:
        print("Invalid choice. You are lost.")
start_scene()
"""


# BROKEN Code Block
player_score = 0 # This is a GLOBAL variable
def  add_points(current_score):
    # Bug: This creates a new LOCAL variable
    player_score = 10
    print(f"[Inside Function] Score is now: {player_score}")
    new_score = current_score + 10
    return new_score

# --- Main Program ---
print(f"[Outside] Player score is: {player_score}")
player_score = add_points(player_score)
print(f"[Outside] Player score is: {player_score}") # Why is it still 0?
