import os

def depositar(deposito,saldo,extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito realizado: (+) R${deposito:.2f}\n"
        print("\nDepósito realizado com sucesso !")
        print(f"Saldo: R${saldo:.2f}\n")
        return saldo, extrato
    else:
        print("\nOperação inválida! Valor digitado inválido")

def sacar(*,saldo,extrato,limite_qtd_saques,VALOR_MAXIMO_SAQUE):
    saque = float(input("Digite o valor que deseja sacar:"))

    saque_maximo_permitido = saque <= VALOR_MAXIMO_SAQUE
    saque_em_saldo_permitido = saque <= saldo

    if not saque_maximo_permitido:
        print(f"\nOperação negada!\nValor acima do limite de R${VALOR_MAXIMO_SAQUE:.2f}\n")

    elif not saque_em_saldo_permitido:
        print("\nOperação negada!\nSaldo insuficiente.\n")

    else:
        saldo -= saque
        extrato +=f"Saque realizado:    (-) R$:{saque:.2f}\n"
        print(f"\nSaque realizado com sucesso!")
        print(f"Saldo: R${saldo:.2f}\n")
        limite_qtd_saques -= 1
    return saldo, extrato, limite_qtd_saques

def criar_usuario(usuarios):
    cpf = valida_cpf(input("Digite o número do seu CPF:"))
    
    possui_cadastro = verificar_usuario(cpf,usuarios)    
    
    if possui_cadastro:
        print("\nEsse CPF já possui um cadastro no DIO-BANK.")
        return usuarios
    else:
        print("\nMuito bem! Vi que deseja fazer o cadastro e ainda não possui conta com a gente",
              "\nVou precisar de algumas informações!")
        nome_completo = input("\nDigite seu nome completo:")+" "
        nome = nome_completo[:nome_completo.index(" ")]
        data_nascimento = input("Digite sua data de nascimento:")
        logradouro = input("Nome da rua:")
        n_residencia = input("Número:")
        bairro = input("Nome do bairro:")
        cidade = input("Cidade:")
        estado = input("Sigla do estado:")
        cadastro = {"nome": nome_completo, "data_nascimento": data_nascimento,"cpf": cpf, "endereco": f"{logradouro}, {n_residencia} - {bairro} {cidade}/{estado}"}
        usuarios.append(cadastro)
        print(f"\nCadastro realizado com Sucesso! Bem vindo {nome} \n")
        return usuarios

def valida_cpf(cpf):
    while not cpf.isdigit():
        print("Erro!... número inválido - O CPF informado deve conter apenas números ")
        cpf = input("Digite o número do seu CPF:")
    return cpf

def verificar_usuario(cpf,usuarios):
    for elemento in usuarios:
        if elemento["cpf"] == cpf:
            return True
    return False

def criar_conta(AGENCIA,n_conta,usuarios):
    cpf = valida_cpf(input("Digite o numero do seu cpf "))
    possui_cadastro = verificar_usuario(cpf,usuarios)

    if possui_cadastro:
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("\nConta registrada com sucesso\n")
                return {"agencia": AGENCIA, "numero_conta": n_conta, "usuario": usuario }
            
    print("\nVoce ainda não é nosso cliente. Por favor, faça um cadastro de usuário para poder abrir uma conta\n")
     
def exibir_extrato(saldo,/,*,extrato):
    print("***************** Extrato Bancário *****************")
    print(f"\n{extrato}")
    print(f"Saldo final R${saldo:.2f}")
    print("****************************************************")

def exibir_contas(contas):
    
    if not contas:
        print("Nenhuma conta registrada")
    else:
        print("Contas cadastradas".center(50,"-"))
        for conta in contas:
            linha = f"Agência:{conta['agencia']}\n" + \
            f"Conta Corrente:{conta['numero_conta']}\n"+\
            f"Titular: {conta['usuario']['nome']}"
            print(linha,"\n")
        

def menu(): 
    menu ='''
    Digite o que deseja realizar:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastro - Novo usuário
    [5] - Cadastro - Nova conta
    [6] - Listar contas 
    [7] - Sair
'''
    print(menu.lstrip())


def main ():
    os.system("cls")
    saldo = 0
    extrato = ""
    limite_qtd_saques = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    VALOR_MAXIMO_SAQUE = 500

    print("BEM VINDO AO DIO-BANK")

    while True:

        menu()
        opcao = input("Opção N°:")    
    #   Depositar
        if opcao == "1":
            deposito = float(input("\nDigite o valor que deseja depositar.\nR$:"))
            saldo, extrato = depositar(deposito,saldo,extrato)

    #   SACAR
        elif opcao == "2":
            print(f"\nSaldo disponivel: R${saldo:.2f}")

            if limite_qtd_saques == 0:
                print("Operação inválida\nN° de saques diários diponíveis já foram realizados!\n")

            else:   
                saldo,extrato,limite_qtd_saques = sacar(saldo=saldo, extrato=extrato, limite_qtd_saques=limite_qtd_saques, VALOR_MAXIMO_SAQUE=VALOR_MAXIMO_SAQUE)
                
    #   Exibir extrato
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)

    #   Cadastro de novo usuário
        elif opcao == "4":
            criar_usuario(usuarios)

    #   Cadastro de nova conta
        elif opcao == "5":
            n_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,n_conta,usuarios)
            if conta:
                contas.append(conta)
    #   Exibir contas
        elif opcao == "6":  
            exibir_contas(contas)
        
    #   Sair 
        elif opcao == "7":
            print("Operação finalizada. Obrigado por ser um cliente da DIO-BANK. Volte sempre")
            break 

        else:
            print("Numero inválido, tente novamente!")
           
main()