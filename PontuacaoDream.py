

class PontuacaoDream(object):
    def __init__(self, tipo_dream):
        self.resultado = self.DadosParaCalculo(tipo_dream)

    def DadosParaCalculo(self, t):
        '''DADOS DE TREINAMENTO'''
        training_data = {}
        training_data["Bem"] = 25
        training_data["Carreira"] = 100
        training_data["EstiloDeVida"] = 15
        training_data["Estudo"] = 40
        training_data["Social"] = 20
        training_data["Lazer"] = 30
        training_data["Saude"] = 50
        training_data["Outros"] = 10
        return training_data[t]
