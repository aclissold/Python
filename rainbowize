#!/usr/bin/env python3

"""Rainbowize makes your boring output SUPER EXCITING™.

To run, if you'd normally run a program like:

    ./foo

or

    python3 foo.py some args and stuff

instead do:

    ./rainbowize.py ./foo

or

    ./rainbowize.py python3 foo.py some args and stuff

.

Note: you are at the mercy of the process you are calling. If that process
buffers its output, rainbowize will not receive any output until flushed.
    
"""

import os
import pty
import subprocess
import sys

class Rainbowizer:
    """A class with which to rainbowize."""
    def __init__(self):
        """Save the color codes to a list and instantiate the process object."""
        self.colors = [
                '\033[38;5;196m', '\033[38;5;202m', '\033[38;5;208m',
                '\033[38;5;214m', '\033[38;5;220m', '\033[38;5;226m',
                '\033[38;5;154m', '\033[38;5;119m', '\033[38;5;120m',
                '\033[38;5;121m', '\033[38;5;122m', '\033[38;5;123m',
                '\033[38;5;117m', '\033[38;5;111m', '\033[38;5;105m',
                '\033[38;5;99m', '\033[38;5;93m']
        self.master, self.slave = pty.openpty()
        self.p = subprocess.Popen(sys.argv[1:], stdin=subprocess.PIPE,
                stdout=self.slave, stderr=self.slave, close_fds=True,
                universal_newlines=True)

    def rainbowize(self):
        """Listen to the output of p and apply color codes to it."""
        # pty is imported and used to bypass the process buffering its stream
        stdout = os.fdopen(self.master)
        i = 0
        while not stdout.closed:
            line = stdout.readline()
            if line != '':
                # Preprend the color to the line
                print(self.colors[i] + line, end='')
                i += 1
                if i == 15:
                    # Reverse the list to avoid counting backwards
                    self.colors.reverse()
                    i = 0

if __name__ == "__main__":
    Rainbowizer().rainbowize()
