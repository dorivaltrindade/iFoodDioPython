import textwrap

def escolheu():
    print(opcoes[opcao], end="... ")

def msg_continuar():
    input("Pressione a tecla [ENTER ] para continuar ...")

def menu():
    menu = """
    ╭───────────────────────────────────────╮
    │     Protótipo de Sistema Bancário     │
    │     ========   M E N U   ========     │
    ╰───────────────────────────────────────╯
    ╭───────────────────────────────────────╮
    │      [ N ]  \t->  Novo Correntista    │
    │      [ C ]  \t->  Nova Conta          │
    │      [ L ]  \t->  Listar Contas       │
    ╰───────────────────────────────────────╯
    ╭───────────────────────────────────────╮
    │      [ D ]  \t->  Depositar           │
    │      [ S ]  \t->  Sacar               │
    │      [ E ]  \t->  Exibir Extrato      │
    ╰───────────────────────────────────────╯
    ╭───────────────────────────────────────╮
    │      [ Q ]  \t->  Sair                │
    ╰───────────────────────────────────────╯
     ==> """
    # opcao = input(menu).upper()
    return input(textwrap.dedent(menu)).upper()

opcoes = {'D': 'Depositar valor', 'S': 'Sacar valor', 'E': 'Exibindo o extrato', 'Q': 'Encerrando o sistema'}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



# TRATANDO_AS_OPERAÇÕES


while True:

    opcao=menu()
    valor = 0

    if opcao == "D":  # DEPOSITAR

        escolheu()
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Dep.: R$ {valor: 0.2f}[+]\n"
            print(f"R$ {valor: 0.2f} depositados com sucesso!\n")
            msg_continuar()
        else:

            print("Operação falhou! O valor informado é inválido.\n")
            msg_continuar()


    elif opcao == "S":  # SACAR

        escolheu()
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print(f"Operação não permitida! Número máximo de {LIMITE_SAQUES} saques foi atingido.\n")
            msg_continuar()
        else:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            if excedeu_saldo:

                print("Operação abortada! Não há saldo suficiente.\n")
                msg_continuar()

            elif excedeu_limite:

                print(f"Operação não permitida! O valor limite de R${limite: 6.2f} por saque não pode ser excedido.\n")
                msg_continuar()

            elif valor > 0:
                saldo -= valor
                extrato += f"Saq.: R$ {valor: 0.2f}[-]\n"
                numero_saques += 1
                print(f"R$ {valor: 0.2f} sacados com sucesso!\n")
                msg_continuar()

            else:
                print(f"O valor R$ {valor: 0.2f} não é válido para a operação de saque!\n")
                msg_continuar()

    elif opcao == "E":  # EXIBIR EXTRATO

        escolheu()
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n__________________________________________")
        print(f"SALDO: R$ {saldo: 0.2f}")
        print("==========================================\n")
        msg_continuar()

    elif opcao == "Q":  # ENCERRAR O SISTEMA
        escolheu()

        break

    else:
        print("Opção não reconhecida! Por favor, selecione outra.\n")
        msg_continuar()
