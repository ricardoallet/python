"""Code contagem de pares de 1 a 50"""
from time import sleep
for c in range(0, 51, 2):
    print(c)
    sleep(0.3)
print('Total de {:.0f} números'.format(c/2))
print('FIM')
