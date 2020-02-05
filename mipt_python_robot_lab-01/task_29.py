#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_7_7():
    flag = True
    while not wall_is_on_the_right() and flag:
        move_right()
        if cell_is_filled():
            for i in range(2):
                if wall_is_on_the_right():
                    break
                move_right()
                if not cell_is_filled():
                    break
                if i == 1:
                    flag = False
                    break


if __name__ == '__main__':
    run_tasks()
