n = int(input("Digite a quantidade de valores: "))
maior = 0

while n > 0:
    x = int(input("Digite um valor: "))
    if x > maior:
        maior = x
    n -= 1

print("Maior:", maior)
