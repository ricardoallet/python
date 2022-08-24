'''Code leia o valor de três segmentos de reta e informe se
é possivel formar um triângulo com eles'''

print('Para se fazer um triângulo, precisamos de três segmentos de reta.')
print('E as condições são: a soma das medidas de dois deles é sempre maior que a medida do terceiro ')
a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))

x = a + b
y = a + c
z = b + c

if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
    print('Com os valores, {:.0f}, {:.0f}, {:.0f} é possível fazer um triângulo, e é retângulo'. format(a, b, c))
elif a == b == c:
    print('Este é um triângulo equilátero com lados de {} cm'.format(a))
elif (x > c) and (y > b) and (z > a):
    print('Com os valores, {:.0f}, {:.0f}, {:.0f} é possível fazer um triângulo escaleno'.format(a, b, c))
else:
    print('Com estes valores não é possível se fazer um triângulo.')



