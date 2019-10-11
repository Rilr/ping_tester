#!/usr/bin/python3

# imports
import subprocess

# definitions
outside = ""
gateway = ""

# ping address, see if we can can do more than one.
# we need to ping google, 8.8.8.8, and the default gateway, 192.168.1.1
for ping in range(1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.Popen(['ping', '-c', '3', address])
    if res == 0:
        print("ping to", address, "OK")
    elif res == 2:
        # output bad pings to file
        print("no response from", address)
    else:
        # output bad pings to file
        print("ping to", address, "failed!")
