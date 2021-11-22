valor_inicial = float(input())

desconto1 = valor_inicial * 0.2

if valor_inicial < 500:
    valor_inicial * 1
elif 500 <= valor_inicial <= 1000:
    desconto2 = valor_inicial * 0.1
elif 1000 < valor_inicial:
    desconto3 = (valor_inicial - 1000) * 0.15 + valor_inicial * 0.1
  
if valor_inicial < 500:
    print("{:.2f}".format(valor_inicial - desconto1))
elif 500 <= valor_inicial <= 1000:
    print("{:.2f}".format(valor_inicial - desconto1 - desconto2))
elif 1000 < valor_inicial:
    print("{:.2f}".format(valor_inicial - desconto1 - desconto3))