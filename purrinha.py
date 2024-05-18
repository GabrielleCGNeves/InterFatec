from functools import reduce

qtd_jogador = int(input())
jogadores = {}


for i in range(qtd_jogador):
    jogadores[input()] = 0

rodadas = int(input())

for i in range(rodadas):
    jogadas_string = input()
    palpites_string = input()

    jogadas = jogadas_string.split(" ")
    palpites = palpites_string.split(" ")

    soma_jogadas = reduce(lambda x, y: int(x) + int(y), jogadas)

    for j in range(len(palpites)):
        if int(palpites[j]) == soma_jogadas:
            jogadores[list(jogadores.keys())[j]] += 1
    
pontos_lista = list(jogadores.values())
pontos_lista.sort()
pontos_lista.reverse()

if pontos_lista[0] != pontos_lista[1]:
    valores = list(jogadores.values())
    indice_ganhador = valores.index(max(valores))
    print(f'{list(jogadores.keys())[indice_ganhador]} GANHOU')
else:
    print('EMPATE')




