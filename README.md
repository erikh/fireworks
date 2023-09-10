This is an attempt at learning python in a fun way. It is not an attempt to
create sustainable open source. You've been warned. :)

This is a TUI "screen saver" that displays fireworks on the terminal. It will
display them until Ctrl+C is pressed and is designed to work with `tmux`, etc,
to provide some bling on your terminal when you only need half of it.

Click [here](https://www.youtube.com/watch?v=Y973e3n8vxk) for a demo on YouTube.

Packaging is probably going to be a mess because I'm a python newbie. Patches
would be welcome here once the project boots as it'd be a good way for me to
experience best practices, but until then chances are you're gonna have your
work cut out for you.

Usage:

-   Clone the repo and `cd` into it
-   `pip install teletype`
-   `python main.py`

I learned a little bit about python and got to create something neat along the way.

Some notes:

-   10 fireworks are launched at start, and every 5 iterations (about half a second) a new one is launched. Fireworks trail north and have a chance of exploding on every frame. Each flare and explosion have random components to the trail and characters used. If the terminal is resized, it clears and rebuilds the scene anew.
-   It is not very nice to your CPU! Maybe I'll fix that someday.
-   I tried to take an asciicast of it but asciicasts.io won't allow uploads that large :) It's quite needy with the terminal.
