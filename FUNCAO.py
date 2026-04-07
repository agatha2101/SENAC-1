
#1
nome = input("Digite o seu nome: ")
def boas_vindas(nome):
    print(f"Bem-vindo(a), {nome}")
boas_vindas(nome)

#2
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

def soma(n1, n2):
    return n1 + n2
resultado = soma(n1, n2)
print(resultado)

#3
n1 = int(input("Digite o primeiro número: "))

def parouimpar(n1):
    if n1 % 2 == 0:
       return "Esse número é par"
    else:
        return "Esse número é impar"
print(parouimpar(n1))

#4
lista = []

while True:
    num = (input("Digite um numero (ou 'sair' para parar): "))

    if num == "sair":
        break

    lista.append(int(num))

def maiornumero(lista):
    return max(lista)
resultado = maiornumero(lista)
print("Maior número: ", resultado)

# 5
palavra = input("Digite uma palavra: ")

def caracteres(palavra):
    return len(palavra)

quantidade = caracteres(palavra)
print(f"Essa palavra tem {quantidade} caracteres")

#6
lista = []

while True:
    num = (input("Digite um numero (ou 'sair' para parar): "))

    if num == "sair":
        break

    lista.append(int(num))

def media(lista):
    return sum(lista) / len(lista)

resultado = media(lista)
print(f"A média dos números é: {resultado}")

#7 NÃO ENTENDI 
def eh_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False

# Exemplo de uso
palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")