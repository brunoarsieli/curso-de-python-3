from random import choice
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input("Qual é a sua jogada? "))

lista = ["PEDRA", "PAPEL", "TESOURA"]

if jogada == 0:
	escolha = lista[0]
elif jogada == 1:
	escolha = lista[1]
elif jogada == 2:
	escolha = lista[2]

jogada_npc = choice(lista)
print('''JO
KEN
PO!!!''')
print(f'''{"-="*12}
Computador jogou {jogada_npc}
Jogador jogou {escolha}
{"-="*12}''')

if escolha == jogada_npc:
	print('EMPATE')
elif escolha == "PEDRA" and jogada_npc == "PAPEL" or escolha == "PAPEL" and jogada_npc == "TESOURA" or escolha == "TESOURA" and jogada_npc == "PEDRA":
	print('COMPUTADOR VENCE')
else:
    print('JOGADOR VENCE')