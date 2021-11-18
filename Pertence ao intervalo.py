x = int(input())
a = int(input())
b = int(input())

pertence_ao_intervalo = False

if a <= x <= b:
    pertence_ao_intervalo = True
else:
    pertence_ao_intervalo = False
    
print(pertence_ao_intervalo)