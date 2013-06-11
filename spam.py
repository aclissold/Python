#1/usr/bin/python3
from time import sleep

out = '*'
while True:
    for i in range(338):
        sleep(0.01)
        print(out)
        out += '*'
    for i in range(338):
        sleep(0.01)
        print(out)
        out = out[:-1]
