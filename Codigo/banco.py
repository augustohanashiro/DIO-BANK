MENU = '''

BEM VINDO AO DIO-BANK

Digite o que deseja realizar:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

Opção N°:'''

saldo = 0
extrato = ""
limite_qtd_saques = 3
VALOR_MAXIMO_SAQUE = 500

while True:

    opcao = input(MENU)

#   Depositar
    if opcao == "1":
        deposito = float(input("\nDigite o valor que deseja depositar.\nR$:"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito realizado: R${deposito:.2f}\n"
            print("\nDepósito realizado com sucesso !")
            print(f"Saldo: R${saldo:.2f}")
        else:
            print("\nOperação inválida! Valor digitado inválido")
            continue

#   SACAR
    elif opcao == "2":
        print(f"Saldo disponivel: R${saldo:.2f}\n")

        if limite_qtd_saques == 0:
            print("Operação inválida\nN° de saques diários diponíveis já foram realizados!\n")

        else:   
            saque = float(input("Digite o valor que deseja sacar:"))
            
            saque_maximo_permitido = saque <= VALOR_MAXIMO_SAQUE
            saque_em_saldo_permitido = saque <= saldo
            
            if not saque_maximo_permitido:
                print(f"\nOperação negada!\nValor acima do limite de R${VALOR_MAXIMO_SAQUE:.2f}")
                
            elif not saque_em_saldo_permitido:
                print("Operação negada!\nSaldo insuficiente.")

            else:
                saldo -= saque
                extrato +=f"Saque realizado de R$:{saque:.2f}\n"
                print(f"Saque realizado de R$:{saque:.2f}")
                print(f"Saldo: R${saldo:.2f}")
                limite_qtd_saques -= 1

    elif opcao == "3":
        print("***************** Extrato Bancário *****************")
        print(f"\n{extrato}")
        print(f"Saldo final R${saldo:.2f}")
        print("****************************************************")
    
    elif opcao == "4":
        print("Operação finalizada. Obrigado por ser um cliente da DIO-BANK. Volte sempre")
        break            
    else:
        print("Numero inválido, tente novamente!")
           


