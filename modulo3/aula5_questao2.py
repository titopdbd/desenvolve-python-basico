l1 = float(input("Digite o comprimento do lado 1: "))
l2 = float(input("Digite o comprimento do lado 2: "))
l3 = float(input("Digite o comprimento do lado 3: "))

if l1 == l2 == l3:
    tipo = "Equilátero"
elif l1 == l2 or l1 == l3 or l2 == l3:
    tipo = "Isóceles"
else:
    tipo = "Escaleno"

print(f"Triângulo: {tipo}")
