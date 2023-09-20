funcionarios = list()
clientes = list()

while True:

    print("\n", "_"*20, "TELA DE LOGON", "_"*20)

    if len(funcionarios) == 0:

        print("\nEsta e a primeira entrada no sistema.\n"
              ""
              "cadastre um funcionario administrador\n")
        # print("\nnenhum funcionario cadastrado")

        func_login: str = input("login: ")
        func_senha: str = input("senha: ")

        funcionario = [func_login, func_senha]
        funcionarios.append(funcionario)

        print("\nfuncionario cadastrado\n")

        # resposta: str = input("Deseja continuar cadastrando funcionarios? (sim ou não) ")

    print("\nPara entrar no sistema informe um login.\n")

    entrada_login_func = input("login: ")

    for i in funcionarios:

        if entrada_login_func == i[0]:

            entrada_senha_func = input("senha:")

            if entrada_senha_func == i[1]:

                print("\nBem Vindo!")



                while True:

                    print("""
    ----------------MENU-----------------
                        
    Para cadastrar um cliente digite [1]
    Para visualizar todos os clientes digite [2]
    Para excluir um cliente digite [3]
    Para pesquisar um cliente digite [4]
    Para fechar o sistema digite [0]
                    
                    """)
                    entrada: str = input("digite a opção desejada: ")



                    if entrada == "1":

                        cliente_nome = input("\nQual o nome do cliente: ")

                        placa = input("Informe a placa: ")

                        cliente = [cliente_nome, placa]
                        clientes.append(cliente)

                        print("\nCliente cadastrado no sitema.")

                    elif entrada == "2":

                        for y in clientes:
                            print(f"Nome: {y[0]}  Placa: {y[1]}")

                    elif entrada == "3":

                        excluir: str = input("\nDigite o nome do cliente que deseja remover: ")
                        contador = 0

                        for x in clientes:

                            if excluir == x[0]:
                                clientes.remove(clientes[contador])
                                print("\nCliente removido com sucesso.")
                                break

                            contador += 1

                            if contador == len(clientes):
                                print("Cliente não encontrado.")

                    if entrada == "4":

                        pesquisa = input("\nQual cliente deseja pesquisar? ")

                        for index in clientes:

                            if index.__contains__(pesquisa):
                                print("Encontrado")
                                break

                            else:
                                print("Cliente não encontrado")


                    if entrada == "0":

                        print("\nVocê saiu do sistema.")
                        break

# ultimo