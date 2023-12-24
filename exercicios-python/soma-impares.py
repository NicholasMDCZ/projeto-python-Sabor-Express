soma_impares = 0 

for numero in range(1,11):
    if numero % 2 != 0:
        soma_impares += numero

print("Soma dos impares de 1 a 10 é igual a: ", soma_impares)