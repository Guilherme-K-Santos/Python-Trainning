import math

f, o, l = [int(w) for w in input().split()]

def farinha(f):
    return (f/2)

def ovo(o):
    return (o/3)

def leite(l):
    return (l/5)

print(math.floor(f/2) ^ math.floor(o/3) ^ math.floor(l/5))
