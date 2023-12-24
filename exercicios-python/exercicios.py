# print('Python na Escola de programação da Alura.')

# nome = 'Nicholas'
# idade = 24

# print(f'Meu nome é {nome} e tenho {idade} anos')

# print('A\nL\nU\nR\nA')

# pi = 3.14159

# print(f'O valor arredondado de pi é: {pi}')

# print('Digite um número')
# numero = int(input())

# if numero % 2 == 0:
    # print("O número é par")
# else:
    # print("O número é ímpar")

# print("qual sua idade?")

# idade = int(input())

# if idade <= 12:
    # print("criança")
# elif idade <= 18:
    # print("adolescente")
# else: print("Adulto")

# usuario = "eu"
# senha = "eu mesmo"

# print("Digite seu nome de usuario")
# login = input()
# print("Digite sua senha")
# senha_de_login = input()

# if usuario == login:
    # print("Usuario correto")
# else:
    # print("Usuario incorreto")

# if senha == senha_de_login:
    # print("Senha correta")
# else:
    # print("Senha incorreta")


print("Fale sua coordenada x")
x = int(input())
print("Fale sua coordenada y")
y = int(input())

if x and y > 0 :
    print("Primeiro quadrante")
elif x < 0 and y > 0 :
    print("Segundo quadrante")
elif x and y < 0 :
    print("Terceiro quadrante")
elif x > 0 and y < 0 :
    print("Quarto quadrante")
else:
    print("O ponto está localizado no eixo ou origem.")