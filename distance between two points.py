import math

x, y = [float(w) for w in input().split()]

x1 = int(x)
y1 = int(y)

a, b = [float(w) for w in input().split()]

x2 = int(a)
y2 = int(b)

def distancia(x1, x2, y2, y1):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

print(distancia(x1, x2, y2, y1))
