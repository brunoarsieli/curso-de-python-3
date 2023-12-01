#Forma de fazer número 1
'''from random import shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f"A ordem de apresentação será:\n{lista}")'''
#Forma de fazer número 2
"""from random import shuffle
lista = []
quantos = int(input("Quantos alunos você deseja sortear? "))
for i in range(quantos):
    lista.append(str(input(f"Digite o nome do {i+1}° aluno: ")))
    
shuffle(lista)
print(f"Os alunos escolhidos foram: {lista}")"""

#Forma de fazer número 3 = definitiva
from random import sample

lista = []

quantos_alunos = int(input("Quantos alunos vão participar do sorteio? "))
quantos_sorteados = int(input("E desses alunos, quantos vão ser sorteados? "))

for i in range(quantos_alunos):
    lista.append(str(input(f"Digite o nome do {i+1}° aluno: ")))
    
sorteados = sample(lista, k=quantos_sorteados)

print(f"Os alunos escolhidos foram: {sorteados}")