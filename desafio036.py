from math import ceil
casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite a renda mensal do comprador: R$ "))
ano = float(input("Em quantos anos você pretende pagar?: "))
conversao = salario * 30 / 100
prestacao = casa / (ano * 12)
print(f"Para pagar uma casa de R${casa} em {int(ano)} anos, a prestação será de: R${prestacao:.2f} ")
if prestacao <= conversao :
    print("Seu empréstimo poderá ser aprovado.")
elif prestacao > conversao:
    print("Empréstimo negado.")
    print(f"Para pagar com o seu salário, iria levar: {casa / (conversao * 12)} anos.")