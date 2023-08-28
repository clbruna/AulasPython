import datetime as dt


# Sistema de estacionamento

print("Faça login para entrar no sistema\n")

nome: str = input("Digite seu nome: ")
senha: str = input("Senha: ")

clientes = list()

if nome in ["pedro", "maria", "santos", "josé"] and senha == "1234":
    print("\nBem vindo")

    while True:

        print("""
                Para registrar a entrada do cliente digite 1
                Para registrar a saída do cliente digite 2
                """)

        menu = input("Digite a opção desejada:")


        if menu == "1":

            nome: str = input("\nNome do cliente:")
            cpf: str = input("CPF:")
            placa: str = input("Placa:")

            # entrada = dt.datetime.now()
            # saida = dt.datetime.now()
            # tempo = entrada - saida

            cliente = [nome, cpf, placa]
            clientes.append(cliente)
        break

        elif menu == "2":

            busca = input("Digite o nome do cliente")

            if busca in clientes == clientes[nome]:
                print("certo")






