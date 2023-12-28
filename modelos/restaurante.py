class Restaurante:
    def __init__(self, nome, categoria):
        nome = ''
        categoria = ''
        ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiano'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

if restaurante_praca.ativo == True:
    print('Restaurante ativo')
else:
    print('Restaurante inativo')
