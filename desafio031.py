distancia = float(input("Digite a distância da viagem: "))
print(f"Você vai percorrer uma viagem de {distancia}Km")
if distancia <= 200:
	preço = distancia * 0.50
else:
	preço = distancia * 0.45
print(f"E o preço da sua passagem vai ser de R${preço:.2f}")








'''distancia = float(input("Digite a distância da viagem: "))
print(f"Você vai percorrer uma viagem de {distancia}Km")
if distancia <= 200:
	print(f"E o preço da sua passagem vai ser de R${distancia * 0.50}")
else:
	print(f"E o preço da sua passagem vai ser de R${distancia * 0.45}")'''