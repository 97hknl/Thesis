import spacy
import sys
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

sys.path.append('../')
from entity import Entity

nlp = spacy.load("en_core_web_sm")
file = open("/home/harsh/Downloads/data/abc_datafiles/01.txt", "r")
text = file.read()
text_nlp = nlp(text)

result = []

for token in text_nlp:
    entity = Entity(token)
    result.append(entity)
    print(token.text, token.pos_, token.dep_)

for entity in result:
    print(entity.token.pos_)

tokenized_word = word_tokenize(text)
fdist = FreqDist(tokenized_word)
print(fdist.most_common(2))
