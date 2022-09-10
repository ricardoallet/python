'''Code Jokenpô'''
'''pedra ganha da tesoura e perde do papel
tesoura ganha do papel'''
from random import randint
from time import sleep

print('{:=^40}'.format(' JO KEN PÔ '))

itens = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
comp = randint (0,2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(0.5)
print('-=' * 12)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' *12)

if comp == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')

elif comp == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')

elif comp ==2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
