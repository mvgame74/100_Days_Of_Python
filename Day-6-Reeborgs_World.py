Code examples for https://reeborg.ca/reeborg.html


Hurdle 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

OR

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -=1

*******************************************************************

HURDLE 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()

*******************************************************************

HURDLE 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()

HURDLE 4A
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def go_up():
    turn_left()
    move()
    turn_right()
    
def go_down():
    turn_right()
    move()
    turn_left()

squares_up = 0
while not at_goal():
    if front_is_clear() and squares_up == 0:
        move()
    if front_is_clear() and squares_up > 0:
        move()
        while squares_up > 0:
            go_down()
            squares_up -= 1
    if wall_in_front():
        go_up()
        squares_up += 1


*******************************************************************


HURDLE 4B

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

*******************************************************************

MAZE

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    else:
        turn_left()

*******************************************************************

MAZE WITH EDGE CASES

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    else:
        turn_left()