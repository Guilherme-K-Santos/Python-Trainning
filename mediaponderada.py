def notafinal(nota_1, nota_2, nota_3, peso_1, peso_2, peso_3):
        return (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3)/(peso_1 + peso_2 + peso_3)

nota_1 = int(input())
nota_2 = int(input())
nota_3 = int(input())
peso_1 = int(input())
peso_2 = int(input())
peso_3 = int(input())

nota_final = notafinal(nota_1, nota_2, nota_3, peso_1, peso_2, peso_3)

print(nota_final > 6)
