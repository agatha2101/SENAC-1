
# 1 [LIST] Lista de compras simples.
listaCompras = ["banana", "maçã", "uva"]
print(listaCompras)

listaCompras.append("morango")
print("O item adicionado foi ", listaCompras)

listaCompras.remove("banana")
print("O item removido foi ", listaCompras)

# 2 [LIST] Remova um número se ele existir

# Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
# Use: int(), input(), in, remove(), len(), print()
# Tipos: int, list.
# Conceitos: teste de pertencimento, tratamento simples de remoção, função len().

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))

lista = [numero1, numero2, numero3, numero4]
print("Tamanho da lista 'lista':", len(lista))
print("Tem o 'numero3'?", numero3 in lista)
lista.remove(numero3)
print("Tamanho da lista 'lista':", len(lista))

# 3 [LIST] Atualizar elemento com uma operação
# Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

lista = [numero1, numero2, numero3]

soma = numero1 + numero2

lista.append(soma)
print(lista)

# 4 [LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média

# Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
# Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
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

novaNota = float(input("Digite uma nova nota para a substituição da menor: "))

lista = novaNota.index(min(lista))

lista.sort()
soma = nota1 + nota2 + nota3
soma /= 3

novaMedia = soma
print("Sua nova média é: ", novaMedia)

# 5 [LIST - desafio] Fila: chegadas, prioridade e atendimento
# Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
# Conceitos: estrutura de fila, operações de inserção/remoção, ordem.

# 6 [DICT] Criar e exibir dicionário de aluno
# Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
# Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
# Tipos: str, int, dict.
# Conceitos: mapeamento chave-valor, criação e exibição.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

aluno = {
    "nome": nome,
    "idade": idade
}

print(aluno)
print(type(aluno))

# 7 [DICT - CONTINUIDADE DO EXERCÍCIO ANTERIOR] 
# Adicionar uma nova chave nota
# Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
# Use: float(), input(), atribuição dict["nota"] = valor, print()
# Tipos: float, dict.
# Conceitos: atualização/adição de chave, tipos numéricos.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

aluno = {
    "nome": nome,
    "idade": idade
}
nota = float(input("Digite a sua nota: "))
aluno["nota"] = nota

print(aluno)

# 8 [DICT] Remover uma chave com segurança

# Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
# Use: input(), float(), dict.pop("chave", valor_padrao), print()
# Tipos: str, float, dict.
# Conceitos: remoção segura, estado antes/depois.

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))

produto = {
    "nome": nome,
    "preco": preco
}

print(produto)


print("Tem 'desconto'? ", "desconto" in produto)
produto.pop("desconto", None)

print(produto)

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

# 10 [DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes
# Tarefa: agenda = {"Ana", "1111-1111", "Bruno": "2222-2222"}
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Remover um contato pelo nome (se existir)
# Exibir a lista ordenada de nomes de contatos
# Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

nome = input("Digite o nome do produto: ")
contato = int(input("Digite seu numero: "))


agenda {
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







