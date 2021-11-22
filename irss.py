salario_bruto = float(input())
dependentes = int(input())

total_dependentes = dependentes * 137.99


if salario_bruto <= 720.00:
     inss = salario_bruto * 0.0765
elif 720.00 < salario_bruto <= 1200.00:
     inss = salario_bruto * 0.09
elif 1200.00 < salario_bruto <= 2400.00:
     inss = salario_bruto * 0.11
elif salario_bruto > 2400.00:
     inss = 2400.00 * 0.11
    
salario_descontado = inss - total_dependentes

if salario_bruto <= 1372.81:
    aliquota = 1
elif 1372.81 < salario_bruto <= 2743.25:
    aliquota = 0.15
elif salario_bruto > 2743.25:
    aliquota = 0.275
    
if salario_bruto <= 1372.81:
    irrf = (salario_bruto - inss - total_dependentes) * aliquota - 0
elif 1372.81 < salario_bruto <= 2743.25:
    irrf = (salario_bruto - inss - total_dependentes) * aliquota - 205.92
elif salario_bruto > 2743.25:
    irrf = (salario_bruto - inss - total_dependentes) * aliquota - 548.82
    
if irrf < 0:
    print(irrf * 0.0)
else: print(irrf)