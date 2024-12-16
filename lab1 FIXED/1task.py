

import random
import sys


A = random.randint(-10, 10)


with open("logs.txt", "a") as log_file:
    log_file.write(f"A = {A}\n")


print(A)