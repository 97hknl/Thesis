import spacy
import sys
import nltk
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
sys.path.append('../')
from entity import Entity

nlp = spacy.load("en_core_web_lg")
file = open("/home/harsh/Downloads/data/abc_datafiles/01.txt", "r")
text = file.read()

text_nlp = nlp(text)
stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
lem = WordNetLemmatizer()
result = []

for token in text_nlp:
    if token.text not in stop_words:
        entity = Entity(token)
        entity.stem = ps.stem(token.text)
        entity.lem = lem.lemmatize(token.text, "v")
        result.append(entity)
        print(entity.lem, entity.token.text, entity.token.pos_)



