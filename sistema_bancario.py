menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""

numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        depositar = -1
        while depositar <= 0:
            depositar = int(input("Digite o valor que deseja depositar: "))
            if depositar <= 0:
                print("Valor inválido, digite um valor positivo")
        saldo += depositar
        extrato += f"Depósito: +{depositar:.2f}.\n"

    elif opcao == "s":
        print("Saque")
        sacar = -1
        if numero_saques < LIMITE_SAQUES:
            while (sacar > limite) or (sacar > saldo) or (sacar < 0) :
                sacar = int(input("Digite o valor que deseja sacar: "))
                if sacar > limite:
                    print(f"O limite de saque é de R${limite:.2f}, digite um valor menor ou igual.")
                
                if sacar > saldo:
                    print("Saldo insuficiente, não será possível realizar a operação")
                
                if sacar < 0:
                    print("Valor inválido, digite um valor positivo.")

            saldo -= sacar
            numero_saques +=1
            extrato += f"Saque: -R${sacar:.2f}.\n"
        else:
            print("Não será possível realizar a operação devido a limite de saques diários atingido.")

    elif opcao == "e":
        print("Extrato")
        if extrato == "":
            print("Não foram realizadas movimentações")
        
        else:
            print(extrato)
            print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
    