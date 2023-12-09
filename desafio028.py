import random

print('-=--='*12)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=--='*12)
numero = random.choice(range(5))
chute = int(input("Em que número eu pensei?"))
print("PROCESSANDO...")
if chute == numero:
    print(f"Você ganhou, o número que pensei era: {numero}")
else:
    print(f"GANHEI! Eu pensei no número {numero} e não no {chute}!")
print(numero)
print("--FIM--")