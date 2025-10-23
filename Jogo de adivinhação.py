from random import randint
from time import sleep
computador = randint(0, 10)
print("Vou pensar em um numero entre \033[1;33m0\033[m e \033[1;33m10\033[m. Tente adivinhar...")
jogador = int(input("Em que numero eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("\033[1mParabéns!\033[m Você conseguiu me vencer!!")
else:
    print("\033[1mQue pena!!\033[m Eu pensei no numero \033[1;33m{}\033[m e não no \033[1;33m{}\033[m!".format(computador, jogador))
