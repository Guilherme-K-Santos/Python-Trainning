def salario(h_normais, h_extra):
    return h_normais * 12.5 + h_extra * 12.5 * 1.2
    
h_normais = float(input())
h_extra = float(input())

salario_bruto = salario(h_normais, h_extra)

print("- Salário Bruto : R$ {:.2f}".format(salario_bruto))
print("- IR (13%) : R$ {:.2f}".format(salario_bruto*0.13))
print("- INSS (9%) : R$ {:.2f}".format(salario_bruto*0.09))
print("- Salário Líquido : R$ {:.2f}".format(salario_bruto*0.78))
