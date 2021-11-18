dias = int(input())

anos = dias//365
meses = dias%365//30
dias = dias%365%30

print(anos,"ano(s)", meses,"mes(es)", dias,"dia(s)")
