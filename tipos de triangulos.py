lado_a = int(input())
lado_b = int(input())
lado_c = int(input())

if lado_a == lado_b == lado_c:
    print("equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("isósceles")
else:
    print("escaleno")