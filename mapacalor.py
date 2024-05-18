from functools import reduce

n_usuarios = int(input())
superior = 0
centro = 0
esquerda = 0
direita = 0
inferior = 0
resultado = ""

for i in range(n_usuarios):
    superior_input = input()
    qtd_superior = superior_input.split(" ")
    qtd_superior = reduce(lambda x, y: int(x) + int(y), qtd_superior)

    superior += qtd_superior

    for j in range(4):
        corpo = input().split(" ")
        esquerda += int(corpo[0])
        centro += int(corpo[1])
        direita += int(corpo[2])


    inferior_input = input()
    qtd_inferior = inferior_input.split(" ")
    qtd_inferior = reduce(lambda x, y: int(x) + int(y), qtd_inferior)

    inferior += qtd_inferior

# print(f"superior: {superior}")
# print(f"esquerda: {esquerda}")
# print(f"centro: {centro}")
# print(f"direita: {direita}")
# print(f"inferior: {inferior}")


print(resultado)