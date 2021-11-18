a = int(input())

def galão(a):
    return max((a * 1/18)/3.6, 1)

def dinheiro(galão):
    return galão * 25

print("-área de cobertura:", a)
print("-número de galões:", round(galão(a)))
print("-valor a ser pago: R$ {:.2f}".format(dinheiro(galão(a))))