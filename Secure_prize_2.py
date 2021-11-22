valor = float(input())
sexo = input()
idade = int(input())

premio = valor * 0.1 

if sexo == "M" and idade <= 24:
    print("{:.2f}".format(premio))
elif sexo == "M" and 25 <= idade <=33:
    print(premio * 0.9)
elif sexo == "M" and 33 < idade:
    print(premio * 0.8)
elif sexo == "F" and idade <= 24:
    print(premio * 0.95)
elif sexo == "F" and 25 <= idade <=33:
    print(premio * 0.8)
elif sexo == "M" and 33 < idade:
    print(premio * 0.65)