peso = float(input("Digite seu peso: (kg) "))
altura = float(input("Digite sua altura: (m) "))
imc = peso / (altura**2)
print(f"O seu IMC é de {imc:.2f}")
if imc < 18.5:
	print("Abaixo do peso")
elif 25 > imc >= 18.5:
	print("Peso ideal")
elif 30 > imc >= 25:
	print("Sobrepeso")
elif 40 > imc >= 30:
	print("Obesidade")
else:
	print("Obesidade mórbida")