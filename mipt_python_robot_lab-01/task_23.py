#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    flag = 0
    while not wall_is_on_the_right():
        move_right()
        flag += 1
        if not wall_is_above():
            take_up_line()
    else:
        move_left(n=flag)


def take_up_line():
    while not wall_is_above():
        move_up()
        fill_cell()
    else:
        fill_cell()
        while not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
