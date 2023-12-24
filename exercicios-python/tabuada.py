numero_digitado = input("Digite o numero da tabuada que gostaria de saber: ")
numero = int(numero_digitado)

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)