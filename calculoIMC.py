nome = input("Nome: ")
peso = float(input("Peso(Kg): "))
altura = float(input("Altura(M): "))

imc = peso / (altura **2)

print(f"IMC de {nome}: {imc:.2f}")

baixo_peso = imc < 18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >= 25) and ( imc < 30)
obesidade = imc >= 30

print("baixo_peso?", baixo_peso)
print("normal?", normal)
print("Sobrepeso?", sobrepeso)
print("Obesidade?", obesidade)