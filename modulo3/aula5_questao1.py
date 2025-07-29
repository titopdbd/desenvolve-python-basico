op1 = float(input("Digite o primeiro operando: "))
operador = input("Digite o operador (+, -, /, *, **): ")
op2 = float(input("Digite o segundo operando: "))

if operador == "+":
    resultado = op1 + op2
elif operador == "-":
    resultado = op1 - op2
elif operador == "*":
    resultado = op1 * op2
elif operador == "/":
    resultado = op1 / op2
elif operador == "**":
    resultado = op1 ** op2
else:
    print("Erro! Operação inválida.")
    exit()

print(f"Resultado: {op1} {operador} {op2} = {resultado}")
