import sys

n = 1
while n < 6:
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    n += 1