# The sentence objects holds a sentence that we may want to embed or tag
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.embeddings import WordEmbeddings
from flair.embeddings import CharacterEmbeddings
from flair.embeddings import BertEmbeddings

file = open("/home/harsh/Downloads/data/abc_datafiles/01.txt", "r")
text = file.read()
text.replace("\"", "\\"")

# load the NER tagger
# Part-of-Speech Tagging
tagger = SequenceTagger.load('pos')

# 4-class Named Entity Recognition
# tagger = SequenceTagger.load('ner')

# Semantic Frame Detection (Experimental)
# tagger = SequenceTagger.load('frame')

# Syntactic Chunking
# tagger = SequenceTagger.load('chunk')

# 12-class Named Entity Recognition
# tagger = SequenceTagger.load('ner-ontonotes')

# run NER over sentence
tagger.predict(text)

#print(sentence)
# print(text.to_tagged_string())

# print('The following NER tags are found:')
# # iterate over entities and print
# for entity in sentence.get_spans('ner'):
#     print(entity)