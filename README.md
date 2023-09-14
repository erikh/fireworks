This is an attempt at learning python in a fun way. It is not an attempt to
create sustainable open source. You've been warned. :)

This is a TUI "screen saver" that displays fireworks on the terminal. It will
display them until Ctrl+C is pressed and is designed to work with `tmux`, etc,
to provide some bling on your terminal when you only need half of it.

Click [here](https://www.youtube.com/watch?v=Y973e3n8vxk) for a demo on YouTube.

Usage:

-   Clone the repo and `cd` into it
-   `pip install -r requirements.txt`
-   `python main.py`

**NOTE:** on OS X you will need homebrew python and then `pip3 install -r
requirements.txt` before things will work. I don't know why, but stock OS X
python doesn't come with the `termios` library that seems to come standard with
python 3.

I learned a little bit about python and got to create something neat along the
way. Big thanks to [@jpetazzo](https://github.com/jpetazzo) for help with
simplifying some of the drawing logic, packaging and general feedback.

Some notes:

-   10 fireworks are launched at start, and every 5 iterations (about half a second) a new one is launched. Fireworks trail north and have a chance of exploding on every frame. Each flare and explosion have random components to the trail and characters used. If the terminal is resized, it clears and rebuilds the scene anew.
-   It is not very nice to your CPU! Maybe I'll fix that someday.
-   I tried to take an asciicast of it but asciicasts.io won't allow uploads that large :) It's quite needy with the terminal.
