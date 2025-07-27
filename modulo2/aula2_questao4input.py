# Lê o valor inteiro
valor = int(input())

# Lista de notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calcula a quantidade de cada nota
for nota in notas:
    qtd = valor // nota
    print(f"{qtd} nota(s) de R${nota},00")
    valor = valor % nota
