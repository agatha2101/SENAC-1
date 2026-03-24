
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

soma = sum(lista) / len(lista)

print("Essa é a sua média:", soma)
print("Menor nota é:", min(lista))

novaNota = float(input("Digite uma nova nota para a substituição da menor: "))

indice = lista.index(min(lista))

lista[indice] = novaNota

lista.sort()

novaMedia = sum(lista) / len(lista)

print("Lista ordenada:", lista)
print("Sua nova média é:", novaMedia)

# 5 [LIST - desafio] Fila: chegadas, prioridade e atendimento
# Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
# Conceitos: estrutura de fila, operações de inserção/remoção, ordem.

fila = ["Ana", "Bruno"]

print("Fila inicial:", fila)

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

fila.extend([nome1, nome2])
print("Após chegadas:", fila)

prioritario = input("Digite o nome do cliente prioritário: ")

fila.insert(1, prioritario)
print("Após prioridade:", fila)

atendido = fila.pop(0)
print("Atendido:", atendido)

print("Fila final:", fila)

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

agenda = {
    "Ana": "1111-1111",
    "Bruno": "2222-2222"
}

print("Agenda inicial:", agenda)

nome = input("Digite o nome para adicionar: ")
tel = input("Digite o telefone: ")

agenda[nome] = tel
print("Após adicionar:", agenda)

nome = input("Digite o nome para atualizar: ")
tel = input("Digite o novo telefone: ")

agenda[nome] = tel
print("Após atualizar:", agenda)

nome = input("Digite o nome para remover: ")

removido = agenda.pop(nome)
print("Removido:", removido)
print("Após remover:", agenda)

ordenados = sorted(agenda.keys())
print("Nomes ordenados:", ordenados)

# 11 [TUPLE] Criar e exibir uma tupla simples
# Tarefa: Leia dois nomes do usuário e coloque-os em uma tupla. Depois exiba a tupla e o tipo dela.
# Orientações: 
# usar input(), print(), type()
# usar tupla no formato (valor1, valor2)
# tipo trabalhado: str, tuple

nome1 = input("Digite o seu nome: ")
nome2 = input("Digite o seu nome: ")

nomes = (nome1, nome2)

print(nomes)

print(type(nomes))

# 12 [TUPLE] Acessar elementos da tupla
# Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
#  Orientações: 
# usar in
# usar input()
# tipo: str, tuple
# conceito: operador de pertinência

fruta1 = input("Digite o nome da fruta: ")
fruta2 = input("Digite o nome da fruta: ")
fruta3 = input("Digite o nome da fruta: ")
 
frutas = (fruta1, fruta2, fruta3)

print("Tem 'maça'?", "maça" in frutas)
print(frutas)

# 13 [TUPLE] Contar quantas vezes um número aparece
# Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
# Orientações: 
# método: tuple.count()
# tipos: int, tuple

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))
n4 = int(input("Digite o número: "))

numeros = (n1, n2, n3, n4)

numeroscount = numeros.count(2)
print(numeroscount)
print(numeros)

# 14 [TUPLE] Exibir maior e menor valor
# Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
#  Orientações: 
# funções: max(), min()
# tipos: int, tuple
# conceito: operações básicas de agregação

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))
n4 = int(input("Digite o número: "))

numeros = (n1, n2, n3, n4)
print(numeros)

print(max(numeros))
print(min(numeros))

# 15 [TUPLE] Dias da semana com tuplas

coordenadas = (10,20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

print(dias)

print("Primeiro dia:", dias[0])
print("Ultimo dia:", dias[-1])
print("Tamanho da tupla 'dias':", len(dias))

print(dias)

# 16 [TUPLE - desafio] Tupla de notas com média (sem alterar a tupla)
# Tarefa: Leia três notas (float) e armazene em uma tupla. Exiba a tupla e a média das notas.
#  Use: float(), sum(), len(), print()
#  Sem alterar tupla.

n1 = float(input("Digite a nota: "))
n2 = float(input("Digite a nota: "))
n3 = float(input("Digite a nota: "))

notas = (n1, n2, n3)

print("Suas notas: ", notas)

soma = n1 + n2 + n3
soma / 3 

print(soma)

# 17 [TUPLE - desafio] Organizar valores sem mexer na tupla original
# Tarefa: Leia quatro números em uma tupla e exiba: 
# a tupla original
# uma lista ordenada apenas para visualizaçã
# o tipo da variável ordenada
# Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))
n4 = int(input("Digite o número: "))

numeros = (n1, n2, n3, n4) 
print(numeros)

ordenados = sorted(numeros)
print("Lista ordenada:", ordenados)

print("Tipo da variável ordenada:", type(ordenados))
