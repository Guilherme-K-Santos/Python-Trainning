a = int(input())
b = int(input())

x = 0
contador = 1

if b > a:
    for _ in range(a, b):
        contador += x + 1
else:
    for _ in range(b, a):
        contador += x + 1
    
print(contador)