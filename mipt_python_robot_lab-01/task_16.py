#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while True:
        fill_cell()

        if not wall_is_on_the_left():
            move_left()
            if cell_is_filled():
                move_right()
                if wall_is_on_the_right():
                    break

        if not wall_is_on_the_right():
            move_right()
            if cell_is_filled():
                move_left()
                if wall_is_on_the_left():
                    break

        if not wall_is_above():
            move_up()


if __name__ == '__main__':
    run_tasks()
