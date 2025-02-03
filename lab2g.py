#!/usr/bin/env python3

# Author: Siu Kit Kong
# Author ID: skkong4
# Date Created: 2025/02/03
import sys
if len(sys.argv) == 1:
    timer = 3
else:
       timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")
