print("Bem-vindo a loja do Samuel Lucas!")
valor1 = float(input("Insira o valor do produto: "))
valor2 = float(input("Insira a quantidade do produto: "))
sem_desconto = valor1 * valor2

if sem_desconto < 2500:
    desconto = 0
elif sem_desconto < 6000:
    desconto = 0.04
elif sem_desconto < 10000:
    desconto = 0.07
else:
    desconto = 0.11

com_desconto = sem_desconto * (1 - desconto)

print("Valor sem desconto:", sem_desconto)
print("Valor com desconto:", com_desconto)




