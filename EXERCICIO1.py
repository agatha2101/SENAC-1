
# 9 [DICT - desafio] Atualizar preço e quantidade; calcular o total 
# Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
# Use: float(), int(), input(), acesso/atribuição por chave, print()
#  Tipos: str, float, int, dict.
#  Conceitos: operadores aritméticos (*, +), atualização de valores no dict.


nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

produto["preco"] = produto["preco"] * 1.6
produto["quantidade"] = produto["quantidade"] + 2

total = produto["preco"] * produto["quantidade"]

print(total)






