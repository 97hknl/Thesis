from nltk.stem import PorterStemmer

class Entity:

    def __init__(self, ent):
        self.obj = ent
        self.text = ent.text
        #explicit
        self.freq = 1
        #implicit
        self.mentions = 0
        self.stem = self.stem()
        self.rank = 0

    def score(self):
        return self.freq + self.mentions + self.rank

    def toString(self):
        result = "[[Text : " + self.text + "]-"
        result += "[Stem : " + self.stem + "]-"
        result += "[Frequency : " + str(self.freq) + "]-"
        result += "[Mentions : " + str(self.mentions) + "]-"
        result += "[Rank : " + str(self.rank) + "]]"

        return result

# approximate string matiching, dice score, hamming distance
    def stem(self):
        stemmed_entity = ""
        porter = PorterStemmer()
        word_list = self.text.split(" ")

        for word in word_list:
            stemmed_entity += porter.stem(word) + " "

        return stemmed_entity.strip();



