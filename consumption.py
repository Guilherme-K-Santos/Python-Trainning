def consumo(km, L):
    return km/L

km = int(input("Quantos kilometros voce andou? "))
L = int(input("quantos litros precisou usar? "))

print(round(km/L, 3),"km/L")
