nome = str(input('Digite seu nome: ')).strip() #strip() - retira todos os espaços antes e depois do nome
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome capitalizado é {}'.format(nome.capitalize()))
print('Seu nome tem ao todo {} letras.'.format((len(nome) - nome.count(' '))))  #len() conta todos os caracteres inclusive espaços,e count() conta tudo o que estiver entre parênteses
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))# find() - pesquisa dentro do objeto selecionado
# outra forma:
separa = nome.split() # split() - coloca o nome dentro de uma lista
print(separa)
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))


