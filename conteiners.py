import math

lc, cc, ac = [int(w) for w in input().split()]

ln, cn, an = [int(w) for w in input().split()]

def altura_limite(ac, an):
    return an/ac
round(an/ac)

def largura_limite(lc, ln):
    return ln/lc
round(ln/lc)

def comprimento_limite(cc, cn):
    return cn/cc
round(cn/cc)

print(math.floor(an/ac) * math.floor(ln/lc) * math.floor(cn/cc))
