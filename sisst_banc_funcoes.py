import textwrap


def escolheu(letra, opcoes):  # OPÇÃO ESCOLHIDA
    print("\n►►►", opcoes[letra], end=" ... \n")


def msg_continuar():  # MENSAGEM DE RETORNO AO MENU
    input("Pressione a tecla [ ENTER ] para retornar ao MENU ...")


def so_numeros(entrada_str):  # REMOVER CARACTER NÃO NUMÉRICO
    aux = entrada_str
    saida_num = (''.join(c for c in aux if c.isdigit()))
    return saida_num


def informar_cpf(cpf):  # CAPTURA PADRÃO PARA CPF
    cpf = input("Digite o CPF (somente números): ")
    if cpf == '':
        print('\n A V I S O: sem informar o CPF a opereção não pode prosseguir!\n')
        return None
    else:
        cpf = so_numeros(cpf)
    return cpf


def menu():  # MENU DO SISTEMA
    menu = """
    ╭───────────────────────────────────────╮
    │     Protótipo de Sistema Bancário     │
    │     ========   M E N U   ========     │
    ╰───────────────────────────────────────╯
    ╭───────────────────────────────────────╮
    │      [ N ]  \t->  Novo Correntista    │
    │      [ O ]  \t->  Listar Correntistas │    
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
     ►►► """
    return input(textwrap.dedent(menu)).upper()


def cadastrar_correntista(correntistas, cpf):                   # CADASTRAR CORRENTISTA

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


def listar_correntistas(correntistas):                          # LISTAR CORRENTISTA
    for correntista in correntistas:
        linha = f"""\
                Nome:               {correntista['nome']}
                Data de Nascimento: {correntista['data_nascimento']}
                CPF:                {correntista['cpf']}
                Endereço:           {correntista['endereco']}
            """
        print("-" * 30)
        print(textwrap.dedent(linha))

    msg_continuar()

    # CRIAR CONTA CORRENTE


def criar_conta_corrente(agencia, numero_conta, correntistas, cpf): # CRIAR CONTA CORRENTE
    correntista = pesquisar_correntista(cpf, correntistas)

    if correntista:
        return {"agencia": agencia, "numero_conta": numero_conta, "correntista": correntista}
    else:
        print(f"\n A V I S O: CPF {cpf} não encontrado!")

        if input(f"\nCadastrar um novo correntista com CPF {cpf} agora? (S/N)")[0].upper() == "S":
            cadastrar_correntista(correntistas, cpf)
            return {"agencia": agencia, "numero_conta": numero_conta,
                    "correntista": correntistas[len(correntistas) - 1]}

    return None


def listar_contas_corrente(contas):                             # LISTA CONTAS CORRENTE
    for conta in contas:
        linha = f"""
                Agência:  {conta['agencia']}
                C/C:      {conta['numero_conta']}
                Titular:  {conta['correntista']['nome']}
                CPF:      {conta['correntista']['cpf']}
            """
        print("-" * 30)
        print(textwrap.dedent(linha))
    msg_continuar()


def depositar(saldo, valor, extrato, /):                        # DEPOSITAR
    if valor > 0:
        saldo += valor
        extrato += f"Dep.: R$ {valor: 0.2f}[+]\n"
        print(f"R$ {valor: 0.2f} depositados com sucesso!\n")

    else:
        print("\n A V I S O: Operação falhou! O valor informado é inválido.\n")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # SACAR
    # TESTAR LIMITE DO NÚMERO DE SAQUES
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saques:
        print(f"Operação não permitida! Número máximo de {limite_saques} saques foi atingido.\n")

    else:
        valor = float(input("Informe o valor do saque: "))
        # TESTAR LIMITE DO SALDO DISPONÍVEL
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print("\n A V I S O: Operação abortada! Não há saldo suficiente.\n")

        elif excedeu_limite:
            print(
                f"\n A V I S O: Operação não permitida! O valor limite de R${limite: 6.2f} por saque não pode ser excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saq.: R$ {valor: 0.2f}[-]\n"
            numero_saques += 1
            print(f"R$ {valor: 0.2f} sacados com sucesso!\n")

        else:
            print(f"\n A V I S O: O valor R$ {valor: 0.2f} não é válido para a operação de saque!\n")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):                           # EXIBIR EXTRATO
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\n__________________________________________")
    print(f"SALDO: R$ {saldo: 0.2f}")
    print("==========================================\n")
    msg_continuar()


def pesquisar_correntista(cpf, correntistas):                       # PESQUISAR CORRENTISTA
    # cria uma lista de correntistas cadastrados
    correntista_existente = [correntista for correntista in correntistas if correntista["cpf"] == cpf]

    # retorna o primeiro correntista que satisfaz a pesquisa pelo CPF
    return correntista_existente[0] if correntista_existente else None
    # se não encontrar ninguém, retorna NONE


def main():                                                         # OPERANDO
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

    opcoes = {'N': 'Cadastrar novo correntista',
              'O': 'Listar correntistas',
              'C': 'Criar nova conta corrente',
              'L': 'Listar contas corrente',
              'D': 'Depositar valor',
              'S': 'Sacar valor',
              'E': 'Exibindo o extrato',
              'Q': 'Encerrando o sistema'}

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    valor = 0
    cpf = ''

    numero_conta = 0
    correntistas = []
    contas = []

    while True:

        letra = menu()

        if not opcoes.get(letra):
            print("\n A V I S O: Opção não reconhecida! Por favor, selecione outra.\n")
            msg_continuar()

        else:
            opcao = letra
            escolheu(opcao, opcoes)

            if opcao == "D":  # DEPOSITAR
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
                msg_continuar()

            if opcao == "S":  # SACAR

                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
                msg_continuar()

            if opcao == "E":  # EXIBIR EXTRATO
                exibir_extrato(saldo, extrato=extrato)

            if opcao == "N":  # NOVO CORRENTISTA
                cpf = informar_cpf(cpf)
                cadastrar_correntista(correntistas, cpf) if cpf != None else msg_continuar()

            if opcao == "O":  # LISTAR CORRENTISTAS
                listar_correntistas(correntistas)

            if opcao == "C":  # CRIAR NOVA CONTA CORRENTE
                cpf = informar_cpf(cpf)
                if cpf != None:
                    numero_conta = len(contas) + 1
                    nova_conta = criar_conta_corrente(AGENCIA, numero_conta, correntistas, cpf)
                    if nova_conta:
                        contas.append(nova_conta)
                        print(
                            f"\n======== Nova Conta criada com sucesso! ========\n\n\t[AG: {AGENCIA}] [C/C: {numero_conta}] [CPF: {correntistas[-1]['cpf']}]\n\t [Correntista: {correntistas[-1]['nome']}]\n")

                msg_continuar()

            if opcao == "L":  # LISTAR CORRENTISTAS
                listar_contas_corrente(contas)

            if opcao == "Q":  # ENCERRAR O SISTEMA
                break


main()                                                              # INICIAR
