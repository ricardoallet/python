'''Code conversor de bases numéricas'''

num = int(input('Digite um valor: '))
print('''Escolha uma base numérica para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Digite sua opção: ' ))
if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'. format(num, hex(num)[2:]))
else:
    print('Opção inválida')
