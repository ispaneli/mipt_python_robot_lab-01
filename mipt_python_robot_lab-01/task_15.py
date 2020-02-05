#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_left() and wall_is_above():
        while not wall_is_on_the_right():
            move_right()
            move_down()
    elif wall_is_on_the_right() and wall_is_above():
        while not wall_is_on_the_left():
            move_left()
            move_down()
    elif wall_is_on_the_left() and wall_is_beneath():
        while not wall_is_on_the_right():
            move_right()
            move_up()
    else:
        while not wall_is_on_the_left():
            move_left()
            move_up()


if __name__ == '__main__':
    run_tasks()
