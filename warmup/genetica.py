def main():
    numero = int(input())
    entrada = input()

    for i in range(len(entrada) - numero + 1):
        fatia = entrada[i:i+numero]
        if fatia == fatia[::-1]:
            print("S")
            break
    if fatia != fatia[::-1]:
        print("N")