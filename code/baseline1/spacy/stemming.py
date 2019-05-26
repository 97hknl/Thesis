import sys
import spacy
from nltk.stem import PorterStemmer
sys.path.append('../')

nlp = spacy.load("en_core_web_lg")
directory = "/home/harsh/Downloads/data/ner-eval-collection-master/plainTextFiles/"
filename = directory +  "0.txt"
file = open(filename, "r")
file_content = file.read()
file_content = file_content.split("<delim>")
article_text = file_content[0]
doc = nlp(article_text)

porter = PorterStemmer()

for ent in doc.ents:
    print(ent)


