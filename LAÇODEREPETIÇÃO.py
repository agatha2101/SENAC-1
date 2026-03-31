precocompras = []

while True:
    preco = float(input("Digite o preço das compras(ou 0 para encerrar): "))
    if preco == 0:
        break

    precocompras.append(preco)

soma = sum(precocompras)
print("Preço final das compras é ", soma)
print ("Você comprou" ,len(precocompras), "itens")

media = soma / len(precocompras)

print("Essa foi a media dos itens que você comprou" ,media)