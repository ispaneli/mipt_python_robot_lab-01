#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not (wall_is_on_the_left() and wall_is_beneath()):
        take_right_line()
        take_left_line()
    else:
        take_right_line()
        take_left_line()


def take_left_line():
    while not wall_is_on_the_left():
        fill_cell()
        move_left()
    else:
        fill_cell()
        if not wall_is_beneath():
            move_down()


def take_right_line():
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    else:
        fill_cell()
        if not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
