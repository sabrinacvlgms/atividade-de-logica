preçoinicial = float(input("digite o preço inicial do produto"))
print("selecione a opção de pagamento: \n 1 - à vista em dinheiro ou cheque \n 2 - à vista no cartão de crédito \n 3 - em duas vezes \n 4 - em tres vezes")
condicao = int(input())
desconto1 = preçoinicial - (preçoinicial*0.10)
desconto2 = preçoinicial - (preçoinicial*0.15)
dividido = preçoinicial + (preçoinicial*0.10)

if condicao == 1:    
    print(desconto1)
elif condicao == 2: 
    print(desconto2)
elif condicao == 3:
    print(preçoinicial)
elif condicao == 4:
    print(dividido)
else:
    print("escolha uma opção valida")