num_palavras = int(input())

telefone = [['A', 'B', 'C'], ['D', 'E', 'F'], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
resultado = []

for i in range(num_palavras):
    temp = ""
    entrada = input()

    for letra in entrada:
        for j in range(len(telefone)):

            for letra_telefone in telefone[j]:

                if letra == letra_telefone:
                    temp += str(j + 2)

    resultado.append(temp)

for valor in resultado:
    print(valor)