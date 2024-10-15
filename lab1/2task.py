import sys
import random

a = float(input())

b = random.randint(-10,10)
if b == 0:
 print("Ошибка: деление на ноль.")
else:
 print(a/b)
