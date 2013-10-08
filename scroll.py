#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Runs in the background on my Awesome setup to display Spotify info."""

import subprocess
import sys
from time import sleep

if __name__ == '__main__':
    spaces = ' ' * 20
    while True:
        try:
            song = subprocess.check_output(['/home/ajclisso/Code/Python/PySpotifyInfo/spotify_control.py', '-d', 'title', 'artist', '-m', ' ~ '], universal_newlines=True)
            song_with_spaces = spaces + song + spaces
            song_with_spaces = song_with_spaces.replace('&', '+')
            song_with_spaces = song_with_spaces.replace("'", "`")
            song_with_spaces = song_with_spaces.replace("ä", "a")
            song_with_spaces = song_with_spaces.replace("\"", "`")

            for i in range(len(song_with_spaces) - 20):
                if song != subprocess.check_output(['/home/ajclisso/Code/Python/PySpotifyInfo/spotify_control.py', '-d', 'title', 'artist', '-m', ' ~ '], universal_newlines=True):
                    print("Failing! Contents of song:", song)
                    break
                display = song_with_spaces[i:i+20]
                subprocess.call(['echo \'spotwidget.text = " ' + display + ' "\' | awesome-client'], shell=True)
                sleep(0.3)
                if i == 20:
                    sleep(2.7)

        except subprocess.CalledProcessError:
            try:
                # Spotify is not running
                display = ''
                subprocess.call(['echo \'spotwidget.text = "' + display + '"\' | awesome-client'], shell=True)
                sleep(10)
            except KeyboardInterrupt:
                display = ''
                subprocess.call(['echo \'spotwidget.text = "' + display + '"\' | awesome-client'], shell=True)
                sys.exit()

        except KeyboardInterrupt:
            display = ''
            subprocess.call(['echo \'spotwidget.text = "' + display + '"\' | awesome-client'], shell=True)
            sys.exit()
