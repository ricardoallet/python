'''Code Calcule o valor do produto se:
A vista, Pix, desc. 10%, deb. 5%, 2x cartão preço normal, mais de 2x 20% juros'''

preço = float(input('Qual o valor do produto: R$ '))
print('Escolha a forma de pagamento:')
print('1 - Dinheiro, Pix \n2 - Débito (1x) \n3 - Cartão (2x) \n4 - Catão (3x ou mais)')
pagto = int(input('Qual a forma de pagamento? '))

pix = float(preço * 0.10)
vista = float(preço * 0.05)
cartao = float(preço * 0.20)
if pagto == 1:
    print('Pagamento a vista. \nPreço: R$ {:.2f} \nVocê economizou R$ {:.2f}'.format((preço - pix), pix))
elif pagto == 2:
    print('Pagamanto em Débito. \nPreço: R$ {:.2f} \nVocê economizou R$ {:.2f}'.format((preço - vista), vista))
elif pagto == 3:
    print('Pagamento em cartão 2x \nPreço: R$ {:.2f} \nValor por parcela: R$ {:.2f}'.format(preço,(preço / 2)))
elif pagto == 4:
    print('Pagamento em cartão \nPreço: R$ {:.2f} \nFoi acrescido R$ {:.2f} pela adm do cartão'.format((preço + cartao), cartao))
print('Obrigado e volte sempre')