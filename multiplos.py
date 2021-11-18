a, b = [int(w) for w in input().split()]

if b%a == 0:
    print("Sao Multiplos")
elif a%b == 0:
    print("Sao Multiplos")
else:
    print("nao sao multiplos")
    