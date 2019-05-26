from nltk.stem import PorterStemmer

class Entity:

    def __init__(self, ent):
        self.obj = ent
        self.text = ent.text
        self.freq = 1
        self.mentions = 0
        self.stem = self.stem()

    def score(self):
        return self.freq + self.mentions

    def toString(self):
        result = "[[Text : " + self.text + "]-"
        result += "[Stem : " + self.stem + "]-"
        result += "[Frequency : " + str(self.freq) + "]-"
        result += "[Mentions : " + str(self.mentions) + "]]"

        return result

    def stem(self):
        stemmed_entity = ""
        porter = PorterStemmer()
        word_list = self.text.split(" ")

        for word in word_list:
            stemmed_entity += porter.stem(word) + " "

        return stemmed_entity.strip();



