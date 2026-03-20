# 10 [DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes
# Tarefa: agenda = {"Ana", "1111-1111", "Bruno": "2222-2222"}
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Remover um contato pelo nome (se existir)
# Exibir a lista ordenada de nomes de contatos
# Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

nome = input("Digite o seu nome: ")
contato = int(input("Digite seu numero: "))


agenda = {
    "nome": nome,
    "contato": contato
}

print(agenda)

agenda["nome"] = "Ana"
agenda["contato"] = 111-222 

print(agenda)

agenda.update({"contato": 111-555 })
print("Agenda após update:", agenda)

removido = nome.pop("nome")

print(agenda)
 
# 10 [DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes
# Tarefa: agenda = {"Ana", "1111-1111", "Bruno": "2222-2222"}
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Remover um contato pelo nome (se existir)
# Exibir a lista ordenada de nomes de contatos
# Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

nome = input("Digite o seu nome: ")
contato = int(input("Digite seu numero: "))


agenda = {
    "nome": nome,
    "contato": contato
}

print(agenda)

agenda["nome"] = "Ana"
agenda["contato"] = 111-222 

print(agenda)

agenda.update({"contato": 111-555 })
print("Agenda após update:", agenda)

removido = nome.pop("nome")

print(agenda)







