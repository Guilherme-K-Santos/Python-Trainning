escala_origem = input()
valor_origem = float(input())
escala_destino = input()

if escala_origem == "c" and escala_destino == "f":
    print((valor_origem * 1.8) + 32)
elif escala_origem == "f" and escala_destino == "c":
    print("{:.6f}".format((valor_origem -32)/1.8))
elif escala_origem == "c" and escala_destino == "k":
    print("{:.2f}".format(valor_origem + 273.15))
elif escala_origem == "k" and escala_destino == "c":
    print("{:.2f}".format(valor_origem - 273.15))
elif escala_origem == "c" and escala_destino == "r":
    print("{:.2f}".format((valor_origem + 273,15) * 9/5))
elif escala_origem == "r" and escala_destino == "c":
    print("{:.2f}".format((valor_origem * 5/9) - 273,15))
elif escala_origem == "f" and escala_destino == "k":
    print("{:.2f}".format((valor_origem + 459.67) * 5/9))
elif escala_origem == "k" and escala_destino == "f":
    print("{:.5f}".format(1.8 * (valor_origem - 273) + 32))
elif escala_origem == "f" and escala_destino == "r":
    print("{:.2f}".format(valor_origem + 459.67))
elif escala_origem == "r" and escala_destino == "f":
    print("{:.2f}".format(valor_origem - 459.67))
elif escala_origem == "k" and escala_destino == "r":
    print("{:.2f}".format(valor_origem * 9/5))
elif escala_origem == "r" and escala_destino == "k":
    print("{:.5f}".format((valor_origem * 5/9)))