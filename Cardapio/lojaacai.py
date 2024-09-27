menu = "Cardápio"


print("Bem-vindo a Loja de Açaí ")
print("-----------------" + menu + "------------------")
print("-------------------------------------------")
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC)|---")
print("---|    P    | R$ 9.00      | R$ 11.00 |---")  
print("---|    M    | R$ 14.00     | R$ 16.00 |---")
print("---|    G    | R$ 18.00     | R$ 20.00 |---")
print("-------------------------------------------")

# Acumulador para somar os valores dos pedidos
total_pedido = 0

# Estrutura de repetição para o pedido de produtos
while True:
    
    sabor = input("Insira o sabor desejado (CP/AC) : ").upper()

    # Verifica se o sabor é válido
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        #Continue para reiniciar o loop
        continue

    #Escolha do tamanho do tamanho
    tamanho = input("Insira o tamanho desejado (P/M/G) : ").upper()

    # Verifica se o tamanho é válido
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        #Continue para reiniciar o loop
        continue

    #Cálculo do valor do pedido
    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 9
        elif tamanho == 'M':
            valor_pedido = 14
        else:
            valor_pedido = 18
    else:  # sabor == 'AC'
        if tamanho == 'P':
            valor_pedido = 11
        elif tamanho == 'M':
            valor_pedido = 16
        else:
            valor_pedido = 20

    # Exibição do pedido atual
    print(f"Pedido: {tamanho} de {sabor} - Valor: R${valor_pedido}")

    #Acumular os valores dos pedidos
    total_pedido += valor_pedido

    #Input para pedido adicional
    continuar = input("Deseja pedir mais alguma coisa? (Digite 's' para sim ou 'n' para não): ").lower()

    # Verificação se o usuário deseja continuar
    if continuar != 's':
        break  #Break para sair do loop

# Exibição do total do pedido
print(f"Total do pedido: R${total_pedido}")