# Lê a temperatura em Fahrenheit (inteiro)
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

# Converte para Celsius usando a fórmula
celsius = int((fahrenheit - 32) * (5 / 9))

# Exibe a mensagem formatada
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
