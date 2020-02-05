#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(n=2)
    for i in range(5):
        make_cross()
        if i != 4:
            move_right(n=2)
    else:
        move_left(n=2)
        move_up()


def make_cross():
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(n=2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()


if __name__ == '__main__':
    run_tasks()
