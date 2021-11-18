nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())

nota_media = (nota_1 + nota_2 + nota_3)/3

if nota_media >= 9.0:
    print("Ótimo")
elif 7.5 <= nota_media < 9.0:
    print("Bom")
elif 6.0 <= nota_media < 7.5:
    print("Satisfatório")
elif 0.0 <= nota_media < 6.0:
    print("Insuficiente")
