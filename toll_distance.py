x, y = [int(w) for w in input().split()]

a, b = [int(w) for w in input().split()]

def custo_por_km(x, a):
    return x * a

def custo_por_pedagios(x, y, b):
    return (x//y) * b

print(custo_por_km(x, a) + custo_por_pedagios(x, y, b))

