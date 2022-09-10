"""Code contagem regressiva"""
from time import sleep
import emoji

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':speaking_head: FELIZ ANO NOVO!!!'))
sleep(1)

for e in range (0,2):
    print(emoji.emojize(10* ':fireworks:'))
    sleep(1)
