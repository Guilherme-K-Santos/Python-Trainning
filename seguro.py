valor_veiculo = float(input())
classe = input()
ind_carro = str(input())
idade = int(input())


val_nacional = valor_veiculo*0.1
val_importado = valor_veiculo*0.15

if indcarro == ('nacional'):
    premio_1 = val_nacional
elif indcarro == ('estrangeira'):
    premio_1 = val_importado
     

premio1_a = premio_1*0.7
premio1_b = premio_1*0.8
premio1_c = premio_1*0.9
premio1_d = premio_1*0.95

if classe == ('A'):
    premio_2 = premio1_a
elif classe == ('B'):
    premio_2 = premio1_b
elif classe == ('C'):
    premio_2 = premio1_c    
elif classe == ('D'):
    premio_2 = premio1_d
elif classe == ('E'):
    premio_2 = premio_1


premio_2_velho = round(premio_2 - premio_1*0.1, 2)
premio_2_novo = round(premio_2, 2)

if idade > 24:
    print(premio_2_velho)
else:
    print(premio_2_novo)