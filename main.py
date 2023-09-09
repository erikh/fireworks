#!/usr/bin/env python
from teletype.io import erase_screen, move_cursor
from termios import tcgetwinsize
from time import sleep
from screen import Screen

iterations = 0
lines, cols = tcgetwinsize(0)
s = Screen(lines, cols)
erase_screen()
while True:
    if iterations == 10:
        newlines, newcols = tcgetwinsize(0)
        if newlines != lines or newcols != cols:
            lines = newlines
            cols = newcols
            s = Screen(lines, cols)
        iterations = 0
    print(s, end="")
    s.randomize()
    move_cursor(-cols, -lines)
    sleep(0.1)
    iterations += 1
