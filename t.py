saldo = 0
extrato = ""
limite_saques = 0
menu= """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

 """


while True:
    opcao= int(input(menu))
    if opcao == 1:
        depositar = int(input("digite o valor desejado: "))
        if depositar < 0:
            print("Valor não é aceito!")
        elif depositar > 0:    
            saldo += depositar
            extrato += f"Deposito de {depositar:.2f}"
            print(f"Foi realizado um deposito no valor de R${depositar:.2f} \nNovo saldo: R${saldo:.2f}")
            

           

    elif opcao == 2:   
        while limite_saques < 3:
            sacar_dinheiro = int(input("digite o valor que deseja sacar: "))
            if sacar_dinheiro > saldo or sacar_dinheiro > 500:
                print("Valor indisponível")
                break
            limite_saques += 1
            saque -= sacar_dinheiro
            extrato += f"Saque de {sacar_dinheiro:.2f}"
            print(f"Saque de {sacar_dinheiro:.2f}")
            print(f"Novo Saldo: {saldo}")
        break

    elif opcao == 3:
        print("EXTRATO")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Valor do saldo: {saldo:.2f}")

    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Comando não reconhecido! Tente novamente")                
        


