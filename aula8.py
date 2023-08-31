# Colections
# List
# Tupla
# Dict
# Set

# Tupla
tupla = (1, 24, 63,74)
# print(tupla[3])

for i in range(len(tupla)):
    print(tupla[i])


# Dicionario/dict
aluno = {"nome": "Carlos", "idade": 34, "RG": "2136813"}
print(aluno["nome"])

# pegando as chaves
chaves = aluno.keys()
print(chaves)

# pegando os valores
valores = aluno.values()
print(valores)

for num, valorTupla in enumerate(tupla):
    print(f"Posição: {num} Valor: {valorTupla}")

print("_"*50)

for num in enumerate(tupla):
    print(num)

print("_"*50)
# Dicionario/dict
# aluno = {"nome": "Carlos", "idade": 34, "RG": "2136813"}
for valor in enumerate(aluno.values()):
    print(valor)

print("_"*50)

for n, valor in enumerate(aluno.values()):
    print(f"número: {n} valor: {valor}")

print("_"*50)

for n, chaves in enumerate(aluno.keys()):
    print(f"número: {n} valor: {chaves}")

print("_"*50)

for chaves, valor in aluno.items():
    if chaves == "idade":
        break
    print(f"Chaves: {chaves} valor: {valor}")

print("_"*50)

for chaves, valor in aluno.items():
    if chaves == "idade":
        continue
    print(f"Chaves: {chaves} valor: {valor}")

print("_"*50)

# adicionar novo valor ao dicionário
aluno["cpf"] = "73332239"

for n, chaves in enumerate(aluno.keys()):
    print(f"número: {n} valor: {chaves}")

print("_"*50)

alunos = [
            {"nome": "Carlos", "idade": 34, "RG": "2136813"},
            {"nome": "Pedro", "idade": 16, "RG": "464555"},
            {"nome": "Maria", "idade": 24, "RG": "685866"}
        ]
print(alunos[1]["nome"])

