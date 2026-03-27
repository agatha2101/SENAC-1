nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))
nota5 = float(input("Digite a quinta nota do aluno: "))

notas = [nota1, nota2, nota3, nota4, nota5]

print(f"Você tem {len(notas)} notas")


soma = nota1 + nota2 + nota3 + nota4 + nota5

media = soma / 5

if media >= 7.0:
    situação = "Aprovado"
else:
    situação = "Recuperação"
print(f"{nome} está: {situação}")
