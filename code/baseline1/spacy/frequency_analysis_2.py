import spacy
import sys
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
sys.path.append('../')
from result import Result
from entity import Entity

# modified frequency analysis - classifies some entity as more important if it has frequency > 1, else less important.
# filters only those which are one of the following: ['PERSON', 'ORG', 'GPE', 'EVENT']

def to_string1(list):
    result = ""

    for element in list:
        result += element.strip() + "\n"

    return result


def to_string2(list):
    result = ""

    for element in list:
        result += element.text + "\t" + str(element.freq) + "\n"

    return result

def contains(entities, entity):
    for item in entities:
        if entity.text in item.text:
            item.freq += 1
            return True
        return False


def report(result):
    directory = "/home/harsh/Downloads/data/ner-eval-collection-master/plainTextFiles/"
    filename = directory + str(result.index) + "-report.txt"
    file = open(filename, "w+")

    file.write(str(result.index) + "\n\n" + result.article_text)

    file.write("\n\nMost Salient Entities\n")
    file.write(to_string1(result.mse))
    file.write("\nLess Salient Entities\n")
    file.write(to_string1(result.lse))

    file.write("\nDetected Most Salient Entities\n")
    file.write(to_string2(result.detected_mse))
    file.write("\nDetected Less Salient Entities\n")
    file.write(to_string2(result.detected_lse))

nlp = spacy.load("en_core_web_lg")
directory = "/home/harsh/Downloads/data/ner-eval-collection-master/plainTextFiles/"
important_entities = ['PERSON', 'ORG', 'GPE', 'EVENT']
results = []

for i in range (0,128):
    filename = directory + str(i) + ".txt"
    file = open(filename, "r")
    file_content = file.read()
    file_content = file_content.split("<delim>")
    article_text = file_content[0]
    doc = nlp(article_text)
    entities = []

    if file_content[1]:
        file_content[1].strip()
        mse_text = file_content[1].replace("[", "").replace("]", "")
        mse_text = mse_text.split(",")

    if file_content[2]:
        file_content[2].strip()
        lse_text = file_content[2].replace("[", "").replace("]", "")
        lse_text = lse_text.split(",")

    article_result = Result(i, article_text, mse_text, lse_text)

    for ent in doc.ents:
        if ent.label_ in important_entities:
            entity = Entity(ent)
            if not contains(entities, entity):
                entities.append(entity)


    for entity in entities:
        if entity.freq > 1:
            article_result.detected_mse.append(entity)
        else:
            article_result.detected_lse.append(entity)

    results.append(article_result)
    # report(article_result)

graph(results)