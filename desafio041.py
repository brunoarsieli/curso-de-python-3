from datetime import datetime
nasc = int(input("Ano de nascimento: "))
atual = datetime.now().year
idade = atual - nasc
if idade <= 9:
    print(f"O atleta tem {idade} anos e pertence a categoria MIRIM.")
elif 14 >= idade > 9:
    print(f"O atleta tem {idade} anos e pertence a categoria INFANTIL.")
elif 19 >= idade > 14:
    print(f"O atleta tem {idade} anos e epertence a categoria JUNIOR.")
elif 25 >= idade > 19:
    print(f"O atleta tem {idade} anos e pertence a categoria SÊNIOR.")
else:
    print(f"O atleta tem {idade} anos e pertence a categoria MASTER.")