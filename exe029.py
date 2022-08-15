'''Escreva um programa que leia a velociade de um carro e se
ultrapassar 80 km/h vai ser multado em R$ 7.00 por km excedente'''

vel = int(input('Indique qual a sua velocidade: '))
vel_perm = (vel - 80)

if vel <= 80:
    print('Velocidade permitida')
else:
    print('Você ultrapassou a velocidade permitida em {} Km e pagará mutla de R$ {:.2f}'.format(vel_perm, (vel_perm * 7)))