'''Code Cálculo de IMC'''
from datetime import date
nome = input('Digite seu nome: ').strip().capitalize()
nasc = int(input('Seu ano de nascimento (yyyy): '))
alt = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
idade = date.today().year - nasc
imc: float = float(peso / (alt * alt))

if imc < 18.5:
    imc2 = ('Magreza')
elif 18.5 <= imc < 25:
    imc2 = ('Normal')
elif 25 <= imc < 30:
    imc2 = ('Sobrepeso')
elif 30 <= imc < 40:
    imc2 = ('Obesidade')
else:
    imc2 = ('Obesidade grave')

print('{}, você tem {} anos, pesa {} Kg e tem {:.2f}m de altura; Seu IMC é igual a {:.1f} e é consederado {}'.format(nome,
                                                                                                                 idade,
                                                                                                                 peso,
                                                                                                                 alt,
                                                                                                                 imc,
                                                                                                                 imc2))
