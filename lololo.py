monstro = 20
jogador = 15
print("Aparece um monstro selvagem e bloqueia seu caminho")
print(f"O monstro tem {monstro} de vida e você tem {jogador}")
while monstro >0 and jogador >0:
    oquefazer = str(input("Digite o que você deseja fazer:(lutar)(nada): "))
    if oquefazer == 'lutar':
        monstro -= 5
        print("Você causou 5 de dano")
        print(f"O monstro agora tem: {monstro} de vida")
        if monstro == 0:
            print("Você venceu! O monstro desmaiou!")
    elif oquefazer == 'nada':
        jogador -= 3
        print("O monstro te causou 3 de dano")
        print(f"Você agora tem apenas: {jogador} de vida")
        if jogador == 0:
            print("Você perdeu!")