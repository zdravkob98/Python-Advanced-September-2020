import math

n = float(input())
base = input()

if base == 'natural':
    print(f'{math.log(n):.2f}')
else:
    base = float(base)
    print(f'{math.log(n, base):.2f}')
