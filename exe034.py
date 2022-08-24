'''Code pergunte quanto recebe de salário e dependendo do valor:
aumento de 10% para salário superior a R$ 1.250,00
aumento de 15% para salário abaixo de R$ 1.250,00'''

sal = float(input('Digite o valor do seu salário: R$ '))

if sal <= 1250:
    print('Você teve um aumento de R$ {:.2f} (15%) no salário, passando a ser R$ {:.2f}'.format(sal * 0.15, sal * 1.15 ))
else:
    print('Você tobteve um aumento de {:.2f} (10%) no salário, passando a ser {:.2f}'.format(sal * 0.10, sal * 1.10))