lado_a = int(input())
lado_b = int(input())
lado_c = int(input())

print((lado_b + lado_c > lado_a) ^ (lado_a + lado_c > lado_b) ^ (lado_b + lado_a > lado_c))
