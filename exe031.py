'''Pergunte a distância de uma viagem em Km e calcule o preço da passagem:
R$ 0.50 por Km se for até 200 Km
R$ 0.45 por Km se for acima de 200 Km'''

km = int(input('Qual a distância da sua viagem em Km? '))

if km <= 200:
    print('O valor da sua passagem é R$ {:.2f}'.format(km * 0.5))
else:
    print('O valor da sua passagem é R$ {:.2f}'.format(km * 0.45))