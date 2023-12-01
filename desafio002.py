name = str(input("Digite seu nome: "))
print("É um prazer te conhecer, {0}!" .format(name))
ask_age = int(input("Digite sua idade: "))
conf_age = str(input("Então você tem {} anos? Digite 's' pra sim e 'n' pra não " .format(ask_age)))
if conf_age == 's' or 'sim':
    print("Ok, sua idade é: {}" .format(ask_age))
else:
    print("Ok, sua idade não é {}." .format(ask_age))
    