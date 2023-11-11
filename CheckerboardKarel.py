from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def work_karel():
    put_beeper()
    move()
    move()
    put_beeper()
def turn_right():
    for i in range(3):
        turn_left()
def move2():
    for i in range(2):
        move()
def main():
    turn_left()
    work_karel()
    move2()
    work_karel()
    move()
    turn_right()
    move()
    turn_right()
    work_karel()
    move2()
    work_karel()
    move()
    turn_left()
    move()
    turn_left()
    work_karel()
    move2()
    work_karel()
    move()
    turn_right()
    move()
    work_karel()
    move2()
    turn_right()
    work_karel()
    move2()
    work_karel()
    move()
    turn_right()
    move()
    work_karel()
    move()
    turn_right()
    move()
    work_karel()
    move2()
    put_beeper()
    move()
    turn_right()
    move()
    work_karel()
    turn_right()
    move2()
    work_karel()
    move()
    turn_right()
    move2()
    turn_right()
    move()
    work_karel()
    move()
    turn_right()
    move()
    turn_right()
    work_karel()
    move2()
    put_beeper()
    turn_right()
    for i in range(5):
        move()
    turn_right()
    for i in range(6):
        move()






    pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
