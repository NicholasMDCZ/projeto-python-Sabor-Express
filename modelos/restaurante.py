class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiano'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]





