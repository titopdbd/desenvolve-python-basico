# Aula 5.1 - Questão 2

import random
import math

n = int(input("Quantos valores aleatórios deseja gerar? "))

soma = 0
for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

raiz = math.sqrt(soma)
print(f"A raiz quadrada da soma dos valores é: {raiz:.2f}")
