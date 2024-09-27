# Sistema Bancário em Python

import sys

# Base de dados
usuarios = {}
contas = []
transacoes = {}

# Funções do menu

def menu():
    print("\n*** Sistema Bancário ***")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Nova Conta")
    print("5. Listar Contas")
    print("6. Novo Usuário")
    print("7. Sair")
    return input("Escolha uma opção: ")

def depositar():
    agencia = input("Informe a agência: ")
    numero_conta = input("Informe o número da conta: ")
    conta = (agencia, numero_conta)
    if conta in contas:
        valor = float(input("Informe o valor do depósito: "))
        transacoes[conta].append(f"Depósito: +{valor}")
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def sacar():
    agencia = input("Informe a agência: ")
    numero_conta = input("Informe o número da conta: ")
    conta = (agencia, numero_conta)
    if conta in contas:
        valor = float(input("Informe o valor do saque: "))
        transacoes[conta].append(f"Saque: -{valor}")
        print("Saque realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def extrato():
    agencia = input("Informe a agência: ")
    numero_conta = input("Informe o número da conta: ")
    conta = (agencia, numero_conta)
    if conta in contas:
        print("Extrato da conta:", conta)
        for transacao in transacoes[conta]:
            print(transacao)
    else:
        print("Conta não encontrada.")

def nova_conta():
    cpf = input("Informe o CPF do usuário: ")
    if cpf in usuarios:
        agencia = input("Informe a agência: ")
        numero_conta = input("Informe o número da nova conta: ")
        conta = (agencia, numero_conta)
        if conta not in contas:
            contas.append(conta)
            transacoes[conta] = []
            print("Conta criada com sucesso!")
        else:
            print("Número de conta já existe.")
    else:
        print("Usuário não encontrado.")

def listar_contas():
    print("Contas cadastradas:")
    for conta in contas:
        print(f"Agência: {conta[0]}, Conta: {conta[1]}")

def novo_usuario():
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
        nome = input("Informe o nome do usuário: ")
        endereco = input("Informe o endereço do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário (DD/MM/AAAA): ")
        usuarios[cpf] = {'nome': nome, 'endereco': endereco, 'data_nascimento': data_nascimento}
        print("Usuário criado com sucesso!")
    else:
        print("Usuário já existe.")

def sair():
    print("Saindo do sistema...")
    sys.exit()

# Programa principal
while True:
    opcao = menu()
    if opcao == '1':
        depositar()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        extrato()
    elif opcao == '4':
        nova_conta()
    elif opcao == '5':
        listar_contas()
    elif opcao == '6':
        novo_usuario()
    elif opcao == '7':
        sair()
    else:
        print("Opção inválida, tente novamente.")


    
