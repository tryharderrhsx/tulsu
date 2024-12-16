import random
import sys

try:
    A = int(sys.stdin.readline().strip())
    B = random.randint(-10, 10)
    with open("logs.txt", "a") as log_file:
        log_file.write(f"B = {B}\n")

    if B == 0:
        raise ZeroDivisionError("Division by zero encountered.")

    result = A / B

    print(result)

except Exception as e:
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error: {str(e)}\n")
    sys.exit(1)