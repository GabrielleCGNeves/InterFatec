entrada = input()
split = entrada.split(" ")

valores = list(map(lambda x: int(x), split))
valores.sort()

print(valores[1])