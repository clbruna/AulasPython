"""
#nome = input("Digite o seu nome: ")
#idade = int(input("Digite a sua idade"))

#while True:
# nota1 = float(input("Digite a sua nota 1: "))
# nota2 = float(input("Digite a sua nota 2: "))
# nota3 = float(input("Digite a sua nota 3: "))
# nota4 = float(input("Digite a sua nota 4: "))
# media = (nota1+nota2+nota3+nota4)/4
# print(media)
# if media >= 8:
# break

#print("Sai do sistema")

# Criar uma aplicação que pega o nome e a idade do aluno verificando se a idade é realmente um int
# varificar se o nome é um str
# faça um loop que force ao aluno a capacidade de cadastrar 4 notas e verifique se as notas são do tipo float
# e se for float converte elas para esse tipo, depois faça a média delas
# se a média for maior que 8 ele sai do loop e manda a mensagem "Você foi aprovado"

#Trabalhando a validação
n="12"
#print(n.isdigit())

#idade=input("Digite a sua idade: ")

#valores Inteiros
#print(idade.isdigit())

#print(idade.isnumeric())

# verificar se é uma letra
#nome=input("digite o seu nome:")
#print(nome.isalpha())

#Alpha Numeric
#numero_Letra="23a45AÇ"
#print(numero_Letra.isalnum())


# para trocar o valor de um caracter eu posso
# usar o metodo replace([vai procurar o valor que deseja mudar],[qual valor que colocar no local])
decimal="12.45"
if str.isdigit(decimal.replace(".","")) or str.isdigit(decimal.replace(",","")) :

 print("antes ",decimal)
 print(type(decimal))
 decimal=float(decimal.replace(",","."))
 print("depois ",decimal)
 print(type(decimal))
else:
 print(type(decimal))"""

usuarios = list()

while True:

 nome = input("Digite o seu nome:")
 senha = input("Digite sua senha:")

 usuario = {"nome": nome, "senha": senha}
 usuarios.append(usuario)

 resposta = input("Deseja cadastrar um novo usuário? (digite sim ou não) ").strip()[0].lower()

 print(resposta)

 if resposta == "n":
  break

print(usuarios)
