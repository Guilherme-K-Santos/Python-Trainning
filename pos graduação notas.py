def equivalente(conceito):
    if conceito == "A":
        nota = 4
    elif conceito == "B":
        nota = 3
    elif conceito == "C":
        nota = 2
    else:
        nota = 0
    return nota
conceito_1 = input()
conceito_2 = input()
conceito_3 = input()
conceito_4 = input()

nota1 = equivalente(conceito_1)
nota2 = equivalente(conceito_2)
nota3 = equivalente(conceito_3)
nota4 = equivalente(conceito_4)

ia = (nota1 + nota2 + nota3 + nota4)/4

if 3 <= ia and conceito_1 != "E" and conceito_2 != "E" and conceito_3 != "E" and conceito_4 != "E":
    aprovacao = True
else:
    aprovacao = False
    
print(aprovacao)