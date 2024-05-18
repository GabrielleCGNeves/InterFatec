entrada = int(input())
resultado = "nao"

for i in range(2, entrada):
    if entrada % i == 0:
        resultado = "sim"
        break

print(resultado)