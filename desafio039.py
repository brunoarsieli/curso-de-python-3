from datetime import datetime
nasc = int(input("Em qual ano você nasceu?: "))
atual = datetime.now().year

if atual - nasc == 18:
    print("Você deverá se alistar esse ano.")
elif atual - nasc < 18:
    print(f"Você deverá se alistar em {nasc + 18} daqui a {nasc + 18 - atual} ano(s)")
else:
    print(f"Você já passou do tempo de se alistar, você deveria ter se alistado no ano de {nasc + 18}, há {atual - (nasc + 18)} ano(s) atrás")