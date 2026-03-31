numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

for num in numeros:

    if num > 10:
        print(f"{num} é maior que 10")
    elif num < 10:
        print(f"{num} é menor que 10")
    else:
        print(f"{num} é igual a 10")