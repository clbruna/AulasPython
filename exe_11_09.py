# SISTEMA DE CADASTRO DE LIVROS
import datetime

# FUNÇÃO PARA FORMATAR LISTA DE LIVROS

def formatar():
    x = 0
    index = 0
    for index in livros[x]:
        print(livro(titulo, autor, editora))
        x += 1


# FUNÇÃO PARA CADASTRO UM LIVRO
def livro(titulo, autor, editora):
    titulo = titulo.strip()
    autor = autor.strip()
    #data = data.strip()
    editora = editora.strip()

    # VALIDAND DICIONÁRIO

    if len(titulo) >= 1:
        if len(autor) >= 1:
            if len(editora) >= 1:

                return {"titulo": titulo, "autor": autor, "editora": editora}

            else:
                print("Digite a editora.")
        else:
            print("Digite o autor.")
    else:
        print("Digite o título.")



livros = list()

while True:

    titulo = input("TÍTULO:")
    autor = input("AUTOR:")
    #data = datetime.datetime.today()
    editora = input("ESITORA:")

    if isinstance(livro(titulo=titulo, autor=autor, editora=editora), dict):
        livros.append(livro(titulo=titulo, autor=autor, editora=editora))

        resposta = input("Desenha cadastrar outro livro? (sim ou não)").strip()[0].lower()

        if resposta == "n":
            break

    else:
        print("Não foi possível cadastrar.")


print(livros)

formatar()
