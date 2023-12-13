seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))
if (seg1 + seg2) > seg3 and (seg2 + seg3) > seg1 and (seg1 + seg3) > seg2:
	print("\033[1;35mÉ um triângulo.\033[0m")
else:
	print("Não é um triângulo.")