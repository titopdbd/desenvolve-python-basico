valor = float(input("Digite o valor total da compra: "))

if valor >= 100:
    desconto = 0.20
elif valor >= 50:
    desconto = 0.10
else:
    desconto = 0.0

valor_final = valor * (1 - desconto)

print(f"Desconto aplicado: {desconto*100:.1f}%")
print(f"Valor final com desconto: R${valor_final:.2f}")
