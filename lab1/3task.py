import math

a = float(input())

if (a>0):
    a=math.sqrt(a)
    with open('output.txt', 'w') as file:
     file.write(str(a))
