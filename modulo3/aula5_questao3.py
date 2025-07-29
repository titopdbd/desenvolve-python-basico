pontos = int(input("Digite a pontuação: "))

if pontos >= 90:
    classificacao = "Excelente"
elif pontos >= 80:
    classificacao = "Bom"
elif pontos >= 70:
    classificacao = "Regular"
else:
    classificacao = "Insatisfatório"

print(f"Classificação: {classificacao}")
