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

def graph(results):
    numMostSalientEntities = []
    numLessSalientEntities = []
    numDetectedMostSalientEntities = []
    numDetectedLessSalientEntities = []
    indices = []

    for result in results:
        numMostSalientEntities.append(len(result.most_salient_entities))
        numLessSalientEntities.append(len(result.less_salient_entities))
        numDetectedMostSalientEntities.append(len(result.detected_most_salient_entities))
        numDetectedLessSalientEntities.append(len(result.detected_less_salient_entities))
        indices.append(result.index)

    plt.xlabel('Article index')
    plt.plot(indices, numMostSalientEntities, label = "Number of Most Salient Entities")
    plt.plot(indices, numLessSalientEntities, label="Number of Less Salient Entities")
    plt.plot(indices, numDetectedMostSalientEntities, label="Number of Detected Most Salient Entities")
    plt.plot(indices, numDetectedLessSalientEntities, label="Number of Detected Less Salient Entities")

    plt.legend()
    plt.show()

def graph2(results):
    indices = []
    percentageExtraMostSalient = []
    percentageExtraLessSalient = []
    percentageLessMostSalient = []
    percentageLessLessSalient = []

    for result in results:
        percentageExtraMostSalient.append(result.percentageExtraMostSalientEntities())
        percentageExtraLessSalient.append(result.percentageExtraLessSalientEntities())
        percentageLessMostSalient.append(result.percentageLessMostSalientEntities())
        percentageLessLessSalient.append(result.percentageLessLessSalientEntities())
        indices.append(result.index)

    plt.plot(indices, percentageExtraMostSalient, label = "Percentage of Most Salient Entities detected extra")
    plt.plot(indices, percentageExtraLessSalient, label = "Percentage of Less Salient Entities detected extra")
    plt.plot(indices, percentageLessMostSalient, label = "Percentage of Most Salient Entities not detected")
    plt.plot(indices, percentageLessLessSalient, label = "Percentage of Less Salient Entities not detected")

    plt.xlabel('Article index')
    plt.legend()
    plt.show()


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
    file.write(to_string1(result.most_salient_entities))
    file.write("\nLess Salient Entities\n")
    file.write(to_string1(result.less_salient_entities))

    file.write("\nDetected Most Salient Entities\n")
    file.write(to_string2(result.detected_most_salient_entities))
    file.write("\nDetected Less Salient Entities\n")
    file.write(to_string2(result.detected_less_salient_entities))




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
        most_salient_entities_text = file_content[1][1:-1]
        most_salient_entities_text = most_salient_entities_text.split(",")

    if file_content[2]:
        file_content[2].strip()
        less_salient_entities_text = file_content[2][1:-1]
        less_salient_entities_text = less_salient_entities_text.split(",")

    article_result = Result(i, article_text, most_salient_entities_text, less_salient_entities_text)

    for ent in doc.ents:
        if ent.label_ in important_entities:
            entity = Entity(ent)
            if not contains(entities, entity):
                entities.append(entity)


    for entity in entities:
        if entity.freq > 1:
            article_result.detected_most_salient_entities.append(entity)
        else:
            article_result.detected_less_salient_entities.append(entity)

    results.append(article_result)
    # report(article_result)

graph(results)