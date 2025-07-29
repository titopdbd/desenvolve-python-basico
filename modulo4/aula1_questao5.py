n = int(input("Digite o número de respondentes: "))
soma = 0
cont = 0

while cont < n:
    idade = int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma += idade
    cont += 1

media = soma / n
print(f"Média das idades: {media:.2f}")
