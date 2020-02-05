#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_6():
    flag = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            flag += 1

        if flag == 5:
            break

        move_right()


if __name__ == '__main__':
    run_tasks()
