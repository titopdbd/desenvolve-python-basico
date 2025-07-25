# MÓDULO 2 – FUNDAMENTOS
# Aula 2.1 – Variáveis – Exercícios

# =============================
# Q1. Quais nomes de variáveis são válidos?
# Resposta: a, c, e, f
#
# Justificativa:
# a) nome_completo → válido
# b) quantidade@produtos → inválido (caractere inválido)
# c) idade → válido
# d) soma idades → inválido (espaço)
# e) MediaNotas → válido
# f) _tipo → válido
# g) 2total → inválido (começa com número)
# h) lambda → inválido (palavra reservada do Python)


# =============================
# Q2. Scripts – Resultado ou erro
print("Q2 - Script 1")
x = 10
y = x + 2
print("Resultado:", y - 5)  # Esperado: 7

print("\nQ2 - Script 2")
# Simulando um script com erro:
try:
    idade = 30
    print(Idade)  # Erro: variável com letra maiúscula não existe
except Exception as e:
    print("Erro:", e)

print("\nQ2 - Script 3")
# Corrigindo um script com erro
nome = "João"
print("Olá,", nome)  # Esperado: Olá, João
