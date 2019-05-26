import spacy
import sys
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

sys.path.append('../')
from entity import Entity

nlp = spacy.load("en_core_web_sm")
file = open("/home/harsh/Downloads/data/abc_datafiles/01.txt", "r")
text = file.read()
text_nlp = nlp(text)
stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
result = []

for token in text_nlp:
    if token.text not in stop_words:
        entity = Entity(token)
        entity.stem = ps.stem(token.text)
        result.append(entity)

for entity in result:
    print(entity.stem, entity.token.text, entity.token.pos_)
