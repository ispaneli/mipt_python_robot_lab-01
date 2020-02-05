#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(6):
        take_right_line()
        take_left_line()


def take_left_line():
    while not wall_is_on_the_left():
        fill_cell()
        move_left()
    else:
        move_right()
        move_down()


def take_right_line():
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    else:
        move_left()
        move_down()


if __name__ == '__main__':
    run_tasks()
