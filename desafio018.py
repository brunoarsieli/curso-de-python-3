from math import radians, sin, cos, tan, pi
an = float(input("Digite um ângulo: "))
sen = sin(an * (3.14/180))
print(f"O ângulo de {an} tem o SENO de {sen:.2f}")
cos = cos(an * (pi/180))
print(f"O ângulo de {an} tem o COSSENO de {cos:.2f}")
tan = tan(radians(an))
print(f"O ângulo de {an} tem a TANGENTE de {tan:.2f}")