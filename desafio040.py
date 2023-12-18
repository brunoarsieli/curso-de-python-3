nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(media)
if media < 5:
	print("REPROVADO")
elif media >= 5 and media <= 6.9:
	print("RECUPERAÇÂO")
else:
	print("APROVADO")