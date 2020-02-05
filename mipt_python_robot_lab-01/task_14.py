#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while not wall_is_on_the_right():
        paint_if_need()
        move_right()
    else:
        paint_if_need()


def paint_if_need():
    if not wall_is_above():
        move_up()
        fill_cell()
        move_down()

    if not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()

    if wall_is_above() and wall_is_beneath():
        fill_cell()


if __name__ == '__main__':
    run_tasks()
