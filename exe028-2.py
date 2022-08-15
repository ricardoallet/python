'''Escreva um programa que faça o comp pensar em um numero inteiro entre 0 e 5
 e peça para o user descobrir qual foi o numero escolhido pelo comp'''

import random
from time import sleep

pc = random.randint(0,5)
user = int(input('Adivinhe o número escolhido de 0 a 5: '))
print("PROCESSANDO...")
sleep(2)
if pc == user:
    print('Você venceu!!! Parabens')
else:
    print('Você perdeu, o número foi {}.... Tente novamente!'.format(pc))

print('=' * 30)