Deposito = 0

Saque = 0

Limite_Saque = 500

numero_Saque = 3

Extrato = Deposito - Saque



print("""Bem vindo a sua conta bancaria! No que podemos te ajudar:

[1]Extrato

[2]Saque

[3]Deposito

[4]Sair

""")



while True:
    menu = input("Digite o número: ")
    if menu == "1":
        print("O Extrato da sua conta é de: R${:.2f}".format(Extrato))
    elif menu == "2":
        if numero_Saque ==0:
            print("Número de Saques atingido, volte outro dia!")
        else:
            numero_Saque = numero_Saque - 1
            Saque = float(input("Qual é o valor do Saque?: "))
            if Saque > Extrato:
                print("Você não pode sacar este valor pois você não possui.")
            else:
                while Saque > Limite_Saque:
                    Saque = float(input("O limite do saque é de R$500.00, por favor digite um número menor ou igual: "))
                    Extrato = Extrato - Saque
    elif menu == "3":
        Deposito = float(input("Qual o valor para Depositar?: "))
        Extrato = Deposito + Extrato
    

    
    elif menu == "4":
        break
    
    else:
        print("Número invalido, por favor digite o número correspondente!")

            


