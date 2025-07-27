# Lê o comprimento do terreno (inteiro)
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Lê a largura do terreno (inteiro)
largura = int(input("Digite a largura do terreno (em metros): "))

# Lê o preço por metro quadrado (float)
preco_m2 = float(input("Digite o preço do metro quadrado da região: "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Exibe o resultado formatado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
