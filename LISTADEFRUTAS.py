frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

frutas.append("morango")
frutas.insert(1, "pera")
print("Após adicionar:", frutas)

frutas.remove("uva")
ultima = frutas.pop()
print("Após remover 'uva e pop():", frutas, "| Última removida:", ultima)

print("Tamanho da lista 'frutas':", len(frutas))

print("Fatiamento [0:2]:", frutas[0:2])

print("Tem 'maçã'?", "maçã" in frutas)