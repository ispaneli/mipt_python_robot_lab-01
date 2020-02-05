#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_2_4():
    move_down()
    for k in range(5):
        for i in range(10):
            make_cross()
            if i != 9:
                move_right(n=2)
        else:
            move_left(n=38)
            if k == 4:
                move_up()
            else:
                move_down(n=4)


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
