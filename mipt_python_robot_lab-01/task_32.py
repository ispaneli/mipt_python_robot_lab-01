#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    answer = 0
    while not wall_is_on_the_right():
        answer += overcome_level()
        move_right()
    else:
        mov('ax', answer)


def overcome_level():
    if wall_is_above():
        fill_cell()
        return 0
    else:
        return take_up_line()


def take_up_line():
    answer = 0
    while not wall_is_above():
        move_up()

        if cell_is_filled():
            answer += 1
        else:
            fill_cell()
    else:
        while not wall_is_beneath():
            move_down()
        else:
            return answer


if __name__ == '__main__':
    run_tasks()
