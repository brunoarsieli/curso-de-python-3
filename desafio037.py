num = int((input("Digite um número inteiro:")))
bin = bin(num)[2:]
oct = oct(num)[2:]
hex = hex(num)[2:]
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input("Sua opção:"))
if escolha == 1:
    escolhido = "BINÁRIO"
    resultado = bin
elif escolha == 2:
    escolhido = "OCTAL"
    resultado = oct
elif escolha == 3:
    escolhido = "HEXADECIMAL"
    resultado = hex
print(f"{num} convertido para {escolhido} é igual a {resultado}")