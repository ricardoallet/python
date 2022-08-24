'''Code simulador de financiamento imobiliário.
Dados: valor da casa, salário, anos para quitar.
Calcule o valor de prestação mensal, sabendo que não pode exceder 30% do salário'''

casa = float(input('Qual o valor da casa a ser financiada em R$: '))
salario = float(input('Qual o seu salário mensal em R$: '))
anos = int(input('Em quantos anos você pretende financiar? '))

meses = anos * 12
prestacao = casa / meses
salario30 = salario * 0.3
print('Você tem R$ {:.2f} disponivel para financiamento'.format(salario30))
if salario30 >= prestacao:
    print('O valor da casa é de R$ {:.2f}, com prestação de R${:.2f} '.format(casa, prestacao), end='')
    print('e será quitada em {} meses'.format(meses))
else:
    print('Infelizmente a prestacao de R$ {:.2f} nao cabe no seu salario'.format(prestacao))