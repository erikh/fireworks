#!/usr/bin/env python
from teletype.io import erase_screen, move_cursor, hide_cursor, show_cursor
from termios import tcgetwinsize
from time import sleep
from screen import Screen
from signal import signal, SIGINT, SIGTERM


def restore_cursor(*args):
    erase_screen()
    show_cursor()
    exit(0)


signal(SIGINT, restore_cursor)
signal(SIGTERM, restore_cursor)

iterations = 0
lines, cols = tcgetwinsize(0)
s = Screen(lines, cols)
erase_screen()
hide_cursor()
while True:
    if iterations == 10:
        newlines, newcols = tcgetwinsize(0)
        if newlines != lines or newcols != cols:
            lines = newlines
            cols = newcols
            s = Screen(lines, cols)
        iterations = 0
    print(s, end="")
    s.tick()
    move_cursor(-cols, -lines)
    sleep(0.1)
    iterations += 1
