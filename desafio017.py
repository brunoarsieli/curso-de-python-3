from math import sqrt, pow, hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
#h = sqrt(co**2+ca**2)
#h = sqrt(pow(co, 2) + pow(ca, 2))
h = hypot(co, ca)
print(f"A hipotenusa vai medir {h:.2f}")