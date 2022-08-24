'''Code alistamento militar
Informe o seu ano de nascimento, e de acordo com a idade:
Ainda vai se alistar e quanto tempo
Está no prazo
Já passou do prazo e quanto tempo'''

from datetime import date
nome = str(input("Qual o seu nome: ")).strip().capitalize()
nasc = int(input('Qual o ano do seu nascimento? '))
data_atual = date.today().year
anos = data_atual - nasc

if anos < 18:
    print('{}, ainda faltam {} anos para seu alistamento'.format(nome, 18 - anos))
elif anos == 18:
    print('{}, já está no prazo do seu alistamento'.format(nome))
else:
    print('{}, ja passaram {} do seu alistamento'.format(nome, anos - 18))

