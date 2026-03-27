inventario = []
while True:
    item = input("Digite um item (ou 'sair' para parar): ")

    if item == "sair":
        break

    inventario.append(item)
inventario.sort()
print(inventario)
print(f"Você tem {len(inventario)} itens no inventário")