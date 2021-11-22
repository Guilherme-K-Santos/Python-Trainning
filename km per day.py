dias = int(input())
km = int(input())

custo_fixo = dias * 45.00

km_por_dia = km/dias

if km_por_dia < 60:
    print(custo_fixo)
else: print(custo_fixo + (km_por_dia - 60) * 0.5 * dias)