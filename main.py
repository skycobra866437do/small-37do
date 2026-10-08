"""A tiny responsive component library using only the standard library."""

import os, sys, signal, time

# initial terminal size
SIZE = os.get_terminal_size()

def resize(signum, frame):
    global SIZE
    SIZE = os.get_terminal_size()

signal.signal(signal.SIGWINCH, resize)

class Component:
    """Base component with a draw method."""
    def draw(self, width, height):
        raise NotImplementedError

class Box(Component):
    """A box that fills the terminal."""
    def draw(self, width, height):
        top_bot = "+" + "-" * (width - 2) + "+"
        middle = "|" + " " * (width - 2) + "|"
        lines = [top_bot] + [middle] * (height - 2) + [top_bot]
        return "\n".join(lines)

def clear():
    sys.stdout.write("\033[H\033[J")

def main():
    box = Box()
    while True:
        clear()
        width, height = SIZE.columns, SIZE.lines
        sys.stdout.write(box.draw(width, height))
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    main()