import math

n = int(input())

def mínimo(n):
    return n/(math.log(n, 2.72))

def máximo(n):
    return 1.25506 * n/(math.log(n, 2.719))

print("{:.1f}".format(mínimo(n)), "{:.1f}".format(máximo(n)))
