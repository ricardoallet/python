#carro = int(input('Quantos anos tem seu carro?'))
#print('Carro novo' if carro<= 3 else 'Carro velho')

nome = str(input('Digite seu nome: ')).strip().capitalize()
sexo = str(input("Qual seu sexo, M(masc.) F(fem.): ")).upper()
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
if (m >= 6.0) and (sexo == 'F'):
    print('{}, Sua nota foi {} e você está aprovada. PARABENS'.format(nome, m))
elif (m >= 6.0) and (sexo == 'M'):
    print('{}, Sua nota foi {} e você está aprovado. PARABENS'.format(nome, m))
elif (m < 6.0) and (sexo == 'F'):
    print('{}, Sua nota foi {} e você está reprovada. ESTUDE MAIS'.format(nome, m))
else:
    print('{}, Sua nota foi {} e você está reprovado. ESTUDE MAIS'.format(nome, m))
