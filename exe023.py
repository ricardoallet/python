num = int(input('Digite um número entre 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
if (num < 0) or (9999 < num):
    print('Fora de escala')
else:
    print('Analisando o número {}, ele tem:'.format(num))
    print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {} '.format(u, d, c, m))

