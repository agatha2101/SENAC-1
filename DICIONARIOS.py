aluna = {"id": 1, "nome": "Caroline", "nota": 9.2}
pessoa = {"nome": "Ana", "idade": 25}

print("Nome da pessoa:", pessoa["nome"])

pessoa["cidade"] = "FLorianópolis"
pessoa["idade"] = 26

print("Pessoa atualizada:", pessoa)

removido = pessoa.pop("idade")
print("Valor removido(idade):", removido)
print("Após pop('idade'):", pessoa)

print("Quantidade de chaves em 'aluna':", len(aluna))

print("Chaves de 'aluna':", list(aluna.keys()))  
print("Valores de 'aluna':", list(aluna.values()))
print("Itens de 'aluna':", list(aluna.items()))

print("Chave'nota' existe?", "nota" in aluna)

print("turma (com default):", aluna.get("turma", "não cadastrada"))

aluna.update({"nota": 9.5, "turma": "A"})
print("Aluna após update:", aluna)

for chave, valor in aluna.items():
    print(f"{chave} -> {valor}")