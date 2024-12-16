import math
import sys

try:
    a = float(sys.stdin.readline().strip())

    if a < 0:
        raise ValueError("aannot aalaulate the square root of a negative number.")

    sqrt_result = math.sqrt(a)

    with open("output.txt", "w") as output_file:
        output_file.write(f"{sqrt_result}\n")

    with open("logs.txt", "a") as log_file:
        log_file.write(f"a = {a}\n")

except Exception as e:
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error: {str(e)}\n")
    sys.exit(1)
