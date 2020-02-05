#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    size = 1
    while not wall_is_on_the_right():
        size += 1
        move_right()

    while size > 2:
        circle(size)
        size -= 2

        move_left()
        move_down()
    else:
        go_to_end()


def circle(size):
    for i in range(size - 2):
        move_down()
        fill_cell()
    move_down()

    for i in range(size - 2):
        move_left()
        fill_cell()
    move_left()

    for i in range(size - 2):
        move_up()
        fill_cell()
    move_up()

    for i in range(size - 2):
        move_right()
        fill_cell()
    move_right()


def go_to_end():
    while not wall_is_on_the_left():
        move_left()
        move_down()


if __name__ == '__main__':
    run_tasks()
