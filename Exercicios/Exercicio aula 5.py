# Criar um programa que gera uma sequência de 1000 números aleatóriamente. Estes números devem ser gerados entre 0 e 10.000.
# Depois o programa deve limpar todos os números repetidos e mostrar na tela a quantidade de números que foram utilzados sem repetição.

import random

numeros = []

for i in range(1000):
    numeros.append(random.randrange(0, 10001))

print(numeros)
print(
    f'A lista original contem {len(numeros)} números, no qual {len(set(numeros))} são únicos e {len(numeros) - len(set(numeros))} são repetidos.')
