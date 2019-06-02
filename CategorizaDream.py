import nltk
from nltk.stem import RSLPStemmer


class CategorizaDream(object):
    def __init__(self, frase):
        self.frase = frase
        self.dados = self.DadosParaTreino()
        self.treino = self.Aprendizado(self.dados)
        self.resultado = self.Scoragem(sentence=self.frase)[0]

    def Aderencia(self, sentence, class_name):
        score = 0
        sentence_ajustada = self.Tokenize(sentence)
        sentence_ajustada = self.Stemming(sentence_ajustada)
        sentence_ajustada = self.RemoveStopWords(sentence_ajustada)
        for word in sentence_ajustada:
            if word in self.treino[class_name]:
                score += self.treino[class_name][word]
        return score

    def Tokenize(self, sentence):
        sentence_ajustada = sentence.lower()
        sentence_ajustada = nltk.word_tokenize(sentence_ajustada)
        return sentence_ajustada

    def Stemming(self, sentence):
        stemmer = RSLPStemmer()
        phrase = []
        for word in sentence:
            phrase.append(stemmer.stem(word.lower()))
        return phrase

    def RemoveStopWords(self, sentence):
        stopwords = nltk.corpus.stopwords.words('portuguese')
        phrase = []
        for word in sentence:
            if word not in stopwords:
                phrase.append(word)
        return phrase

    def DadosParaTreino(self):
        '''DADOS DE TREINAMENTO'''
        training_data = []
        training_data.append({"classe": "Bem", "frase": "quero trocar de carro"})
        training_data.append({"classe": "Bem", "frase": "comprar nova tv"})
        training_data.append({"classe": "Bem", "frase": "mudar de casa"})
        training_data.append({"classe": "Carreira", "frase": "pedir promocao"})
        training_data.append({"classe": "Carreira", "frase": "trocar de emprego"})
        training_data.append({"classe": "Carreira", "frase": "consegui um emprego"})
        training_data.append({"classe": "EstiloDeVida", "frase": "raspar o cabelo"})
        training_data.append({"classe": "EstiloDeVida", "frase": "fazer cirurgia"})
        training_data.append({"classe": "EstiloDeVida", "frase": "pintar um quadro"})
        training_data.append({"classe": "Estudo", "frase": "cursar faculdade"})
        training_data.append({"classe": "Estudo", "frase": "fazer um curso"})
        training_data.append({"classe": "Estudo", "frase": "aprender ingles"})
        training_data.append({"classe": "Social", "frase": "conhecer mais pessoas"})
        training_data.append({"classe": "Social", "frase": "participar de eventos"})
        training_data.append({"classe": "Social", "frase": "fazer novos amigos"})
        training_data.append({"classe": "Lazer", "frase": "viajar para india"})
        training_data.append({"classe": "Lazer", "frase": "fazer uma festa"})
        training_data.append({"classe": "Lazer", "frase": "conhecer outro pais"})
        training_data.append({"classe": "Saude", "frase": "consultar um medico"})
        training_data.append({"classe": "Saude", "frase": "Ir na academia"})
        training_data.append({"classe": "Saude", "frase": "correr pela manha"})
        training_data.append({"classe": "Outros", "frase": "eu nao sei o que quero fazer"})
        print("%s frases incluidas" % len(training_data))
        return training_data

    def Aprendizado(self, training_data):
        corpus_words = {}
        for data in training_data:
            frase = data['frase']
            frase = self.Tokenize(frase)
            frase = self.Stemming(frase)
            frase = self.RemoveStopWords(frase)
            class_name = data['classe']
            if class_name not in list(corpus_words.keys()):
                corpus_words[class_name] = {}
            for word in frase:
                if word not in list(corpus_words[class_name].keys()):
                    corpus_words[class_name][word] = 1
                else:
                    corpus_words[class_name][word] += 1
        return corpus_words

    def Scoragem(self, sentence):
        '''DEFINE O GRUPO'''
        high_score = 0
        classname = 'Outros'
        for classe in self.treino.keys():
            pontos = 0
            pontos = self.Aderencia(sentence, classe)
            if pontos > high_score:
                high_score = pontos
                classname = classe
        return classname, high_score


if __name__ == '__main__':
    f = 'preciso de um carro novo'
    test = CategorizaDream(frase=f)
    print(test.resultado)
