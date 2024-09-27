#uma string multilinha que armazena o menu de opções para o usuário.
menu = """

|__________________|
|                  |
|   [1] Depositar  |
|   [2] Sacar      |
|   [3] Extrato    |
|   [4] Sair       |
|__________________|
|                  |

"""

saldo = 0          #Variável que armazena o saldo da conta, inicializada com o valor zero.
limite = 2000      #Variável que define o limite de saque da conta, inicializada com o valor 500.
extrato = ""       #Uma string que armazena o extrato das transações realizadas na conta.
numero_saques = 0  #Variável que armazena o número de saques realizados, inicializada com o valor zero.
LIMITE_SAQUES = 3  #Constante que define o número máximo de saques permitidos.



while True:        #Inicia um loop infinito que executa o código dentro dele repetidamente até que a instrução break seja alcançada.

    opcao = input(menu)   #Solicita ao usuário que selecione uma opção do menu e armazena a entrada do usuário na variável opcao.

#Estrutura if, elif, else: Verifica a opção selecionada pelo usuário e executa o código correspondente.
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: ")) #1 o programa solicita ao usuário o valor do depósito e atualiza o saldo e o extrato.

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2": 
        valor = float(input("Informe o valor do saque: ")) #2 solicita ao usuário o valor do saque e verifica se é possível realizar a operação de acordo com as condições.

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":  #3 exibe o extrato das transações e o saldo atual da conta.
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":  #4 o programa encerra o loop e sai do programa.
        break           #Encerra o loop infinito quando o usuário seleciona a opção "4".

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        #Se nenhuma das opções acima for selecionada, uma mensagem de operação inválida é exibida.