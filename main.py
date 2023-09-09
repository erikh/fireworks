#!/usr/bin/env python
from teletype.io import erase_screen, move_cursor
from termios import tcgetwinsize
from time import sleep
from screen import Screen

erase_screen()
while True:
    lines, cols = tcgetwinsize(0)
    s = Screen(lines, cols)
    print(s, end="")
    move_cursor(-cols, -lines)
    sleep(0.05)
