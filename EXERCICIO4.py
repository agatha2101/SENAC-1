#1
num = int(input("Digite um número: "))

if num >= 1:
    print("Seu número é positivo")
elif num <= -1:
    print("Seu número é negativo")
else:
    print("Seu número é zero")

#2
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

#3
idade = int(input("Digite a sua idade: "))

if idade <= 11:
    print("Você é uma criança")
elif idade > 11 and idade <= 17:
    print("Você é um adolescente")
elif idade >17 and idade <= 59:
    print("Você é adulto")
else:
    print("Você é idoso")

#4
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")

#5
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

if num1 > num2:
    print("O primeiro número é maior que o segundo")
elif num1 == num2:
    print("Seus números são iguais")
else:
    print("O segundo número é maior que o primeiro")

#6 
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

operacao = input("Digite a operação (+, -, /, *): ")

if operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
elif operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
