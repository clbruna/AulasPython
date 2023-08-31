# Sistema de controle

usuarios = list()

while True:

    nome = input("Digit o seu nome:")
    rg = input("Digite seu RG:")
    ano_nasc = input("Digite o ano em que você nasceu:")

    telefones = list()

    tel1 = input("Digite seu primeiro número de telefone:")
    telefones.append(tel1)

    tel2 = input("Digite seu segundo número de telefone:")
    telefones.append(tel2)

    print("Cadastrar despesas:")
    descricao = input("Descrição da despesa:")
    valor = float(input("Valor da despesa:"))

    dicionario = {"nome": nome, "RG": rg, "ano": ano_nasc, "telefones": telefones, "despesas": {"descricao": descricao, "valor": valor}}
    usuarios.append(dicionario)

    resposta = input("Deseja continuar? sim ou não").strip()[0].lower()

    if resposta == "n":
        break

print(usuarios)
