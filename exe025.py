nome = str(input('Digite seu nome: ')).strip()
proc = str(input('Digite o nome que deseja procurar: ')).upper().strip()
print('Seu nome tem {}? {}'.format(proc, proc in nome.upper()))
