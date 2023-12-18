seg1 = float(input("Digite o comprimento do primeiro segmento: "))
seg2 = float(input("Digite o comprimento do segundo segmento: "))
seg3 = float(input("Digite o comprimento do terceiro segmento: "))
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg3 + seg1 > seg2:
    if seg1 == seg2 == seg3:
        print("É um triângulo equilátero.")
    elif seg1 == seg2 != seg3 or seg2 == seg3 != seg1 or seg3 == seg1 != seg2:
        print("É um triângulo isósceles.")
    elif seg1 != seg2 != seg3 != seg1:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")