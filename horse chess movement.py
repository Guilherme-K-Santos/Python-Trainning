x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

cavalo = False

if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
    cavalo = True
    
elif abs(y1 - y2) == 2 and abs(x1 - x2) == 1:
    cavalo = True
else:
    cavalo = False

print(cavalo)
