#!/usr/bin/python2

"""Runs in the background on my Awesome setup to display Spotify info.

Uses deprecated Python 2 techniques.

"""

import os
import commands
import subprocess
from time import sleep

if __name__ == '__main__':
    spaces = ' ' * 20
    while True:
        song = commands.getstatusoutput('spotout.sh')[1]
        if song != 'SPOTIFY' and song != '':
            song_with_spaces = spaces + song + spaces
            song_with_spaces = song_with_spaces.replace('&', '+')
            song_with_spaces = song_with_spaces.replace("'", "`")
            for i in range(len(song_with_spaces) - 20):
                if song != commands.getstatusoutput('spotout.sh')[1]:
                    print("Failing! song, spotout.sh:")
                    break
                display = song_with_spaces[i:i+20]
                subprocess.call(['echo \'spotwidget.text = " ' + display + ' "\' | awesome-client'], shell=True)
                sleep(0.3)
                if i == 20:
                    sleep(2.7)
        else:
            display = ''
            subprocess.call(['echo \'spotwidget.text = "' + display + '"\' | awesome-client'], shell=True)
            sleep(10)
