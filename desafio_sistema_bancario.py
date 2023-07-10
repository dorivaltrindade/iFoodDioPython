def escolheu():
    print(opcoes[opcao], end="... ")


opcoes = {'D': 'Depositar valor', 'S': 'Sacar valor', 'E': 'Exibindo o extrato', 'Q': 'Encerrando o sistema'}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
┌─────────────[ DIGITE UMA TECLA ]────────────┐
│                                             │
│  [ D ]  ->  D e p o s i t a r               │
│                                             │
│  [ S ]  ->  S a c a r                       │
│                                             │
│  [ E ]  ->  E x i b i r   E x t r a t o     │
│                                             │
│  [ Q ]  ->  S a i r                         │
└─────────────────────────────────────────────┘
 ==> """

# TRATANDO_AS_OPERAÇÕES


while True:

    opcao = input(menu).upper()
    valor = 0

    if opcao == "D":  # DEPOSITAR

        escolheu()
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Dep.: R$ {valor: 0.2f}[+]\n"
            print(f"R$ {valor: 0.2f} depositados com sucesso!\n")
            input("Pressione a tecla [ E N T E R ] para continuar ...")
        else:

            print("Operação falhou! O valor informado é inválido.\n")
            input("Pressione a tecla [ E N T E R ] para continuar ...")


    elif opcao == "S":  # SACAR

        escolheu()
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print(f"Operação não permitida! Número máximo de {LIMITE_SAQUES} saques foi atingido.\n")
            input("Pressione a tecla [ E N T E R ] para continuar ...")
        else:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            if excedeu_saldo:

                print("Operação abortada! Não há saldo suficiente.\n")
                input("Pressione a tecla [ E N T E R ] para continuar ...")

            elif excedeu_limite:

                print(f"Operação não permitida! O valor limite de R${limite: 6.2f} por saque não pode ser excedido.\n")
                input("Pressione a tecla [ E N T E R ] para continuar ...")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saq.: R$ {valor: 0.2f}[-]\n"
                numero_saques += 1
                print(f"R$ {valor: 0.2f} sacados com sucesso!\n")
                input("Pressione a tecla [ E N T E R ] para continuar ...")

            else:

                print(f"O valor R$ {valor: 0.2f} não é válido para a operação de saque!\n")

    elif opcao == "E":  # EXIBIR EXTRATO

        escolheu()
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n__________________________________________")
        print(f"SALDO: R$ {saldo: 0.2f}")
        print("==========================================\n")
        input("Pressione a tecla [ E N T E R ] para continuar ...")

    elif opcao == "Q":  # ENCERRAR O SISTEMA
        escolheu()

        break

    else:
        print("Opção não reconhecida! Por favor, selecione outra.\n")
        input("Pressione a tecla [ E N T E R ] para continuar ...")
