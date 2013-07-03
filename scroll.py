#!/usr/bin/python3
import os
from time import sleep
song = 'Man on Fire ~ Edward Sharpe & the Magnetic Zeros'
spaces = ' ' * len(song)
while True:
    for i in range(len(song)):
        os.system('clear')
        print(song[i:] + spaces[:i])
        sleep(1 / 10)
    for i in range(len(song)):
        os.system('clear')
        print(spaces[i:] + song[:i])
        sleep(1 / 10)
