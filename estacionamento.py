"""
usuarios = list()
cadastro_logins = set()
# clientes = list()

while True:

    print(            Menu Principal
            __________________________________________
            Para cadastrar um novo usuário digite 1.
            Para fazer login digite 2.
            Para localizar um usuário digite 3
            Para encerrar digite 4.)

    menu = int(input("Selecione a opçaõ desejada:"))

    if menu == 1:

        while True:

            user = input("Digite um nome para login:")
            senha = input("Digite uma senha:")

            usuario = {"usuario": user, "senha": senha}
            usuarios.append(usuario)

            print([usuario.values()])

            print("Deseja cadastrar um novo usuário? (digite sim ou não)")
            resposta = input().strip()[0].lower()

            if resposta == "n":
                break

    elif menu == 2:

        print(usuarios[usuario]["user"])
        print("Faça login com usuário e senha para acessar o sistema.")

        login_user = input("Usuário:")
        # login_senha = input("Senha:")


        if login_user in usuarios == :
            print("certo")

        else:
            print("Errado")

    elif menu == 4:
        pass

    else:
        print("Digite apenas uma das opções")



print(usuarios)"""

usuarios = list()
logins_cadastrados = {"bruna"}

print("\n", "_" * 20, "MENU", "_" * 20)

print(f"""
Para fazer login digite[1]
Para cadastrar um novo usuário digite [2]
Para encerrar digite [3]
""")

print("_" * 46)

while True:

    menu: str = input("Digite a opção desejada:")

    if menu == "1":

        login_entrar = input("Login:")

        for index in usuarios:

            if login_entrar == index[0]:
                print("Bem vindo!")
                break

            # elif login_entrar != index[0]:
                # print("Usuario ou senha incorretos!")

            else:
                print("Usuario ou senha incorretos!")
                break


    elif menu == "2":

        print("\n", "_" * 12, "CADASTRO DE USUÁRIO", "_" * 12)

        print("Para cadastrar um novo usuário digite um login e senha.")
        print("_" * 46)

        while True:

            login: str = input("login:")

            if login in logins_cadastrados != login:

                print("Usuário já cadastrado")
                print(logins_cadastrados)

            else:

                senha: str = input("senha:")

                usuario = [login, senha]

                logins_cadastrados.add(login)
                usuarios.append(usuario)

            resposta: str = input("Deseja cadastrar um novo usuário? (sim ou não)").strip()[0].lower()

            if resposta == "n":
                break

    elif menu == "3":
        break

    else:
        print("Digite uma das opções!")
        print("_" * 46)

print(usuarios)
print(logins_cadastrados)
