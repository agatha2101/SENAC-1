# 4 [LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média

#Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
#Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
# Tipos: float, list.
# Conceitos: mutabilidade, ordenação in-place, média aritmética.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

lista = [nota1, nota2, nota3]

soma = nota1 + nota2 + nota3
soma /= 3

print("Essa é a sua média:", soma)
print("Menor nota é: ", min(lista))

novaNota = input("Digite uma nova nota para a substituição da menor: ")

lista = novaNota.index(min(lista))

lista.sort()
soma = nota1 + nota2 + nota3
soma /= 3

novaMedia = soma
print("Sua nova média é: ", novaMedia)