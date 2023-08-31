validar = set()
logins = list()

print("sistema de cadastro")
while True:
    usuario = list()
    login = input("Login: ")
    tamanho = len(validar)

    if login.strip()[0].lower() == "e":
        break

    validar.add(login)

    if len(validar) == tamanho:
        print(f"login ja exite")
    else:
        senha = input("senha: ")
        usuario.append(login)
        usuario.append(senha)
        logins.append(usuario)

while True:
    entrada_login =input ("Login: ")
    entrada_senha = input("senha:")

    for i in logins:
        if entrada_login == i[0] and entrada_senha == i[1]:
            print("bem vindo")
        else:
            print("login ou senha incorreta")
            break



