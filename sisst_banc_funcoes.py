import textwrap


def escolheu(letra, opcoes):

    print(opcoes[letra], end="... ")


def msg_continuar():
    input("Pressione a tecla [ ENTER ] para continuar ...")


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


def cadastrar_correntista(correntistas):
    cpf = input("Digite o CPF (somente números): ")

    novo_correntista = pesquisar_correntista(cpf, correntistas)

    if novo_correntista:
        print(f"\n A V I S O: o CPF [ {cpf} ] já está cadastrado na base!\n")
        msg_continuar()
        return
    else:
        nome_completo = input("Digite o nome completo: ")
        data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
        endereco_completo = input("Digite o endereço completo (logradouro, n.º - bairro - cidade/UF): ")
        correntistas.append({"nome": nome_completo,
                             "data_nascimento": data_nascimento,
                             "cpf": cpf,
                             "endereco": endereco_completo})

        print(f"\nCliente , {cpf}, cadastrado com sucesso!\n")
        msg_continuar()

def criar_conta_corrente():
    print("Função não programada!")
    msg_continuar()

def listar_contas_corrente():
    print("Função não programada!")
    msg_continuar()

def pesquisar_correntista(cpf, correntistas):

    # cria uma lista de correntistas cadastrados
    correntista_existente = [correntista for correntista in correntistas if correntista["cpf"] == cpf]

    # retorna o primeiro correntista que satisfaz a pesquisa pelo CPF
    return correntista_existente[0] if correntista_existente else None
    # se não encontrar ninguém, retorna NONE

def main():

    opcoes = {'N': 'Cadastrar novo correntista',
              'C': 'Criar nova conta corrente',
              'L': 'Listar contas correte',
              'D': 'Depositar valor',
              'S': 'Sacar valor',
              'E': 'Exibindo o extrato',
              'Q': 'Encerrando o sistema'}

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    correntistas = []
    contas = []

    # TRATANDO_AS_OPERAÇÕES


    while True:

        opcao = menu()
        valor = 0
        escolheu(opcao,opcoes)

        if opcao == "D":  # DEPOSITAR


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

            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print("\n__________________________________________")
            print(f"SALDO: R$ {saldo: 0.2f}")
            print("==========================================\n")
            msg_continuar()

        elif opcao == "Q":  # ENCERRAR O SISTEMA
            break

        elif opcao == "N":
            cadastrar_correntista(correntistas)

        elif opcao =="C":
            criar_conta_corrente()

        elif opcao =="L":
            listar_contas_corrente()

        else:
            print("Opção não reconhecida! Por favor, selecione outra.\n")
            msg_continuar()

main()  # colocando o sistema em funcionamento