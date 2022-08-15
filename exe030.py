'''Leia um numero inteiro e diga se é par ou impar'''

num = int(input('Digite um número para saber se é par ou impar: '))
x = num % 2

if x == 0:
    print("{} é um número par".format(num))
else:
    print('{} é um número impar'. format(num))