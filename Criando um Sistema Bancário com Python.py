deposito = 0
saque = 0
numeroSaque = 3
saldo = 0
extrato = ""

print("Bem vindo ao sistema bancario!!!")
while True:
    print("""
----------------------------------------------

[1]Extrato

[2]Saque

[3]Deposito

[4]Sair
----------------------------------------------
""")

    menu = input("Digite o número: ")
    if menu == "1":
        print("\n----------------------------------------------")
        print(extrato)
        print("Saldo = R${:.2f}\n ".format(saldo))

    elif menu == "2":
        if numeroSaque == 0:
            print("Número de Saques atingido, volte outro dia!")
        else:
            numeroSaque = numeroSaque - 1
            saque = float(input("Qual é o valor do Saque?: "))
            if (saque > saldo) or (saque < 0):
                print("Você não pode sacar este valor pois é invalido.")
            else:
                if saque > 500:
                    print("O limite do saque é de R$500.00, por favor digite um número menor ou igual: ")
                else:
                    saldo = saldo - saque
                    print("Feito o saque de: R${:.2f}".format(saque))
                    extrato += f"Saque-> R${saque:.2f}\n"
                    
    elif menu == "3":
        deposito = float(input("Qual o valor para Depositar?: "))
        if deposito < 0:
            print("Você não pode depositar este valor pois é invalido.")
        else:
            saldo = saldo + deposito
            print("Feito o deposito de: R${:.2f}".format(saque))
            extrato += f"Deposito-> R${deposito:.2f}\n"

    elif menu == "4":
        break
    
    else:
        print("Número invalido, por favor digite o número correspondente!")

            

