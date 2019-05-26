import nltk
import spacy
import sys
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

sys.path.append('../')
from entity import Entity


def contains(result, text):
    for item in result:
        if item.text in text or text in item.text:
            item.freq += 1
            return True
    return False


nlp = spacy.load("en_core_web_sm")
file = open("/home/harsh/Downloads/data/ner-eval-collection-master/temp.txt", "r")
text = file.read()

doc = nlp(text)
stop_words = set(stopwords.words("english"))

result = []
unimportant_entities = ['WORK_OF_ART', 'LAW', 'LANGUAGE', 'DATE', 'TIME', 'PERCENT', 'QUANTITY', 'ORDINAL', 'CARDINAL']

for ent in doc.ents:
    if ent.label_ not in unimportant_entities:
        entity = Entity(ent)
        if not contains(result, ent.text):
            result.append(entity)

# for token in doc:
#     if token.text not in stop_words and \
#             (token.pos_ =='ADJ' or
#              token.pos_ == 'NOUN' or
#              token.pos_ == 'PROPN'):
#         entity = Entity(token)
#         # entity.stem = ps.stem(token.text)
#         # entity.lem = lem.lemmatize(token.text, "v")
#
#         if not contains(result, token.text):
#             result.append(entity)

# print(entity.lem, entity.token.text, entity.token.pos_)

result.sort(key=lambda x: x.freq, reverse=True)

for item in result:
    print(item.text, item.freq)

# print("****************************************")
#
# for chunk in doc.noun_chunks:
#     print(chunk.text, chunk.root.text, chunk.root.dep_,
#             chunk.root.head.text)
#
# print("****************************************")
