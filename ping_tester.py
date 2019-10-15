#!/usr/bin/python3

# imports
from os import system
from time import sleep
from time import ctime

# definitions
hostnames = [
    '192.168.0.1',
    '8.8.8.8',
]

# loop through the list
while True:
    for hostname in hostnames:
        sleep(30)
        response = system('ping -n 3 ' + hostname)
        if response == 0:
            print(hostname + ' is up')
        else:
            print(ctime() + ": " + hostname + ' is down.', file=open("output.txt", "a"))
