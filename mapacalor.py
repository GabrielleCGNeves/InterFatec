n_usuarios = int(input())

regioes = [0, 0, 0, 0, 0]
resultado = ""

for i in range(n_usuarios):
    superior_input = input()
    qtd_superior = 0
    qtd_inferior = 0
    qtd_superior_temp = superior_input.split(" ")

    for num in qtd_superior_temp:
        qtd_superior += int(num)

    regioes[0] += qtd_superior

    for j in range(4):
        corpo = input().split(" ")
        regioes[1] += int(corpo[0])
        regioes[2] += int(corpo[1])
        regioes[3] += int(corpo[2])


    inferior_input = input()
    qtd_inferior_temp = inferior_input.split(" ")

    for num in qtd_inferior_temp:
        qtd_inferior += int(num)

    regioes[4] += qtd_inferior

maior_valor = max(regioes)
maior_regiao = regioes.index(maior_valor)

if maior_regiao == 0:
    resultado = "superior"
if maior_regiao == 1:
    resultado = "esquerda"
if maior_regiao == 2:
    resultado = "centro"
if maior_regiao == 3:
    resultado = "direita"
if maior_regiao == 4:
    resultado = "inferior"

print(resultado)