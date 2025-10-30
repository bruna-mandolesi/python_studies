from random import randint
v = 0
while True:
    jogador = int(input("Digite um valor de 0 e 10: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {v} vezes.")
