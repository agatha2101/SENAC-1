nota = float(input("Digite a sua nota: "))

if nota < 5: 
    categoria = "Reprovada"
elif nota >5 and nota <= 6.9:
    categoria = "Recuperação"
elif nota >7 and nota <= 8.9:
    categoria = "Aprovada"
else:
    categoria = "Aprovada com excelência"
print((f"{categoria}"))
