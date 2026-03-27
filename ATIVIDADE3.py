notas = []

while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota <= -1:
        break

    notas.append(nota)

soma = sum(notas)
media = soma / len(notas)

print(media)

if media >= 7.0:
    situação = "Aprovado"
else:
    situação = "Recuperação"
print(situação)
