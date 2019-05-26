from nltk.stem import PorterStemmer

class Entity:

    def __init__(self, ent):
        self.obj = ent
        self.text = ent.text
        self.freq = 1
        self.score = 0
        self.stem = self.stem()

    def toString(self):
        result = "[[Text : " + self.text + "]-"
        result += "[Stem : " + self.stem + "]-"
        result += "[Frequency : " + str(self.freq) + "]]"

        return result

    def stem(self):
        stemmed_entity = ""
        porter = PorterStemmer()
        word_list = self.text.split(" ")

        for word in word_list:
            stemmed_entity += porter.stem(word) + " "

        return stemmed_entity.strip();



