import spacy
import sys
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

sys.path.append('../')
from entity import Entity

nlp = spacy.load("en_core_web_sm")
file = open("/home/harsh/Downloads/data/abc_datafiles/01.txt", "r")
text = file.read()
text_nlp = nlp(text)
stop_words = set(stopwords.words("english"))
result = []

for token in text_nlp:
    if token.text not in stop_words:
        entity = Entity(token)
        result.append(entity)

for entity in result:
    print(entity.token.text, entity.token.pos_)
