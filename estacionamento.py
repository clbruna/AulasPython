usuarios = list()

while True:

    print("Menu principal\n\n"
          "Para fazer login digite 1\n"
          "Para cadastrar um usuário digite 2\n"
          "Para remover um usuário digite 3\n"
          "Para localizar um usuario digite 4\n"
          "Para sair do sitema digite 5\n")

    menu = int(input("Selecione a opçaõ desejada:"))

    if menu == 2:
        print("Cadastrando novo usuário\n")

        nome = input("Digite seu nome:")
        senha = input("Digite sua senha:")

        usuario = [nome, senha]
        usuarios.append(usuario)

    elif menu == 4:
        print("Localizar usuário")

        pesquisa = input("Digite o nome do usuário:")

        if usuarios[usuario.count(pesquisa)]:
            print(usuarios)

        else:
            print("Usuário não cadastrado")

    elif menu == 1:
        print("Faça login\n\n")

        login_usuario = input("Usuário:")
        # login_senha = input("Senha:")

        if menu == 0:
            print("entrou no sitema")

        else:
            print("usuario ou senha incorretos")


    elif menu == 5:
        break

print(usuarios)
