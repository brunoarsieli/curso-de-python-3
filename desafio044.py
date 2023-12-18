print("============ Loja Vende Tudo ============")
preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input("Qual é a opção? "))
if opção == 1:
	desconto = preço * (10 / 100)
	print(f"Sua compra de R${preço} vai custar R${preço - desconto} no final.")
elif opção == 2:
    desconto = preço * (5 / 100)
    print(f"Sua compra de R${preço} vai custar R${preço - desconto} no final.")
elif opção == 3:
    print(f"Sua compra vai custar R${preço}.")
elif opção == 4:
    parcela = int(input("Deseja parcelar em quantas vezes? "))
    juros = (preço * (20 / 100)) 
    print(f"Sua compra vai ser parcelada em {parcela}x de R${(preço + juros) / parcela} COM JUROS")
    print(f"Sua compra de R${preço} vai valer R${preço + juros} no final.")