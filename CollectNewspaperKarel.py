from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def turn_right():
    for i in range(3):
        turn_left()
def turn1():
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
def back():
    while front_is_clear():
        move()
    turn_right()
    move()
    put_beeper()
    turn_right()
def main():
    turn1()
    turn_left()
    turn_left()
    back()
    pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
