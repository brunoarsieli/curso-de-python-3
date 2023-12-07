frase = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra A aparece {frase.count("A")} vezes na frase")
print(frase.find("A")+1)
print(frase.rfind("A")+1-frase.count(" "))