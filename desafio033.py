pv = int(input("Digite o primeiro valor: "))
sv = int(input("Digite o segundo valor: "))
tv = int(input("Digite o terceiro valor: "))
valor_mais_alto = 0
valor_mais_baixo = 0
if pv > sv and pv > tv:
    valor_mais_alto = pv
if sv > pv and sv > tv:
    valor_mais_alto = sv
if tv > pv and tv > sv:
    valor_mais_alto = tv
if pv < sv and pv < tv:
    valor_mais_baixo = pv
if sv < pv and sv < tv:
    valor_mais_baixo = sv
if tv < pv and tv < sv:
    valor_mais_baixo = tv
print(f"{'-'*24}\nValor mais alto digitado: {valor_mais_alto}")
print(f"Valor mais baixo digitado: {valor_mais_baixo}")
print("--FIM--")