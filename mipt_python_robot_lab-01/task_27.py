#!/usr/bin/python3

from pyrob.api import *

# [2, 3, 5, 8, 12, 17, 23, 30, 38]
# [1, 2, 4, 7, 11, 16, 22, 29, 37]
#  [1,  2, 3, 4,  5,  6,  7,  8]
@task(delay=0.01)
def task_7_5():
    move_right()
    fill_cell()
    delta = 1
    while not wall_is_on_the_right():
        try:
            move_right(delta)
        except Exception:
            break

        if wall_is_on_the_right():
            break

        fill_cell()
        delta += 1


if __name__ == '__main__':
    run_tasks()

