'''Programa que le três números e mostra qual é o maior e qual o menor'''

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {}.'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {}.'.format(maior))