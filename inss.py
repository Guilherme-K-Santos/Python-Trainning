salario_bruto = float(input())


if salario_bruto <= 720.00:
    print(salario_bruto * 0.0765)
elif salario_bruto <= 1200.00:
    print(salario_bruto * 0.09)
elif salario_bruto <= 2400.00:
    print(salario_bruto * 0.11)
elif salario_bruto >= 2400.00:
    print(2400 * 0.11)