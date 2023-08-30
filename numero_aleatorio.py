from random import randint
from time import sleep
valor = input('Digite um número entre 0 e 3: ')
for c in range(0,3):
    print('...')
    sleep(1)
print(f'Você escolheu o número {valor}, eu escolhi {randint(0, 3)}')
