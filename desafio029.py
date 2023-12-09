v = int(input("Digite a velocidade atual do carro em km/h:"))
multa = 7 * (v - 80)
if v > 80:
	print(f"MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê estava dirigindo {v-80}km/h a mais do que o permitido \nEntão deverá pagar uma multa de R${multa}!")
else:
    print("Você estava andando na velocidade permitida e não irá ser multado.")
print("Tenha um bom dia! Dirija com segurança!")
print("--FIM--")    