placa = input()
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prefixo = placa[0:3]
qtd_letras = 0

for letra in prefixo:
    is_letra = not letra.isnumeric()

    if is_letra:
        qtd_letras += 1

print(qtd_letras)
