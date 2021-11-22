kwh = int(input())

if kwh <= 30:
    classificacao = kwh * 0.09556
elif 30 < kwh <= 100:
    classificacao = 30 * 0.09556 + (kwh - 30) * 0.16698
elif 100 < kwh <= 200:
    classificacao = 30 * 0.09556 + 70 * 0.16698 + (kwh - 100) * 0.25052
elif kwh > 200:
    classificacao = 30 * 0.09556 + 70 * 0.16698 + 100 * 0.25052 + (kwh - 200) * 0.27836

print("{:.2f}".format(classificacao))
