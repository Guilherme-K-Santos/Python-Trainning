comprimento = float(input())
largura = float(input())
gavetas = int(input())
madeira = input()

metro_2 = comprimento * largura * 100.00

if metro_2 < 200:
    mesa = metro_2 * 1
elif metro_2 > 200:
    mesa = metro_2 + 50.00
    
    
if madeira == "mogno":
    mesa_madeira = mesa + 150.00
elif madeira == "carvalho":
    mesa_madeira = mesa + 125.00
else: mesa_madeira = mesa
    
preco_final = mesa_madeira + gavetas * 30


print("{:.2f}".format(preco_final))