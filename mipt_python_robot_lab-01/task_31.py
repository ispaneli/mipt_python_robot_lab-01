#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        while not wall_is_beneath():
            move_down()

        flag = overcome_level()

        if not flag:
            while not wall_is_on_the_left():
                move_left()
            else:
                break


def overcome_level():
    if search_hole():
        while not wall_is_beneath():
            move_down()
        else:
            return True
    else:
        return False


def search_hole():
    while not wall_is_on_the_right():
        if not wall_is_beneath():
            return True
        move_right()
    else:
        while not wall_is_on_the_left():
            if not wall_is_beneath():
                return True
            move_left()
        else:
            return False


if __name__ == '__main__':
    run_tasks()
