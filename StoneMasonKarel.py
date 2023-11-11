from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def turn_right():
    for i in range(3):
        turn_left()
def go_head4():
    for i in range(4):
        move()
def main():
    put_beeper()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    for i in range(2):
        move()
    turn_right()
    go_head4()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
    put_beeper()
    for i in range(2):
        move()
    turn_left()
    go_head4()
    turn_left()
    put_beeper()
    move()
    put_beeper()
    for i in range(2):
        move()
    put_beeper()
    move()
    turn_right()
    go_head4()
    turn_right()
    move()
    put_beeper()
    for i in range(2):
        move()
    put_beeper()
    move()
    turn_left()
    pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
