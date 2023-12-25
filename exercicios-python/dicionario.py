dicionario = {'Nome': 'Nicholas Castro', 'Idade': 24, 'Cidade': 'Curitiba'}

dicionario['Idade'] = 99

dicionario['classe'] = 'Mago'

del dicionario['Cidade']

print(dicionario)


dicionario_numerico = {'Primeiro': 1, 'Segundo': 2, 'Terceiro': 3, 'Quarto': 4, 'Quinto': 5}

for chave, valor in dicionario_numerico.items():
    dicionario_numerico[chave] = valor * valor

if 'Primeiro' in dicionario_numerico:
    print("existe")
else:
    print("Não existe")

print(dicionario_numerico)