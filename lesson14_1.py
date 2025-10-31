# LESSON #14. Модули в языке Python. Создание и работа с модулями

import datetime as dt
import os
import sys
import random
import platform
import time
import cowsay
from lesson14_2 import hello as hi
from math import sqrt, ceil

# time

time.sleep(1)

# datetime
print("\ndatetime:\n" + '-' * 50)

print(
    f"Day: {dt.datetime.now().day} ({dt.datetime.now().weekday()})\n"
    f"Month: {dt.datetime.now().month}\n"
    f"Year: {dt.datetime.now().year}\n\n"
    f"Hours: {dt.datetime.now().hour}\n"
    f"Minutes: {dt.datetime.now().minute}\n"
    f"Seconds: {dt.datetime.now().second}")

# sys
print("\nsys:\n" + '-' * 50)

print(f"sys.path: {sys.path}")

# os
print("\nos:\n" + '-' * 50)

print(f"os.name: {os.name}")

# platform
print("\nplatform:\n" + '-' * 50)

print(f"platform.system(): {platform.system()}")

# random
print("\nrandom:\n" + '-' * 50)

print(f"random.randint(-256, 256): {random.randint(-256, 256)}")

# math
print("\nmath:\n" + '-' * 50)

print(f"ceil(s(25)): {ceil(sqrt(25))}")

# lesson14_2
print("\nlesson14_2:\n" + '-' * 50)

hi("Alex")

# cowsay
print("\ncowsay:\n" + '-' * 50)

print(cowsay.get_output_string('cow', 'Mooooo~'))
