temperatura = float(input("Digite a temperatura: "))

if temperatura < 10:
    categoria = "Muito frio"
elif temperatura >= 10 and temperatura < 24:
    categoria = "Agradável"
elif temperatura >= 25 and temperatura < 30:
    categoria = "Quente"
else: 
    categoria = "Muito quente"
print(f"temperatura - {categoria}")