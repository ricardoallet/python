'''Code classificação de atletas por faixa etária'''

from datetime import date
nasc = int(input('Qual seu ano de nascimento? '))
idade: int = date.today().year - nasc
print('Você está com {} anos e sua categoria é:'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade == 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')

