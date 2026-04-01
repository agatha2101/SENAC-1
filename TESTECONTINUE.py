senha = ''

while True:
    senha = input("Digite uma senha: ")

    if len(senha) < 6:
        print("Senha muito curta!")
        continue 

    print("Senha valida!")
    break