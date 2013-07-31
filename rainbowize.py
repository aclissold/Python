#!/usr/bin/env python3

import sys

colors = ["\033[38;5;160m", "\033[38;5;202m", "\033[38;5;11m",
    "\033[38;5;10m", "\033[38;5;4m", "\033[38;5;5m"]

def rainbowize():
    i = 0
    for line in sys.stdin.readlines():
        print(colors[i] + line, flush=True, end="")
        i += 1
        if i == 6:
            i = 0

if __name__ == "__main__":
    rainbowize()
