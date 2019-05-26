import matplotlib.pyplot as plt
import spacy
import sys

sys.path.append('../')
from result import Result
from entity import Entity
from graphs import Graphs


# simple frequency analysis - classifies some entity as more important if it has frequency > 1, else less important.

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
        if entity.text == item.text:
            item.freq += 1
            return True
        return False


def contains_stem(entities, entity):
    for item in entities:
        if entity.stem in item.stem or item.stem in entity.stem:
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


def stemmed_frequency_analysis(doc, article_result):
    important_entities = ['PERSON', 'ORG', 'GPE', 'EVENT']
    entities = []

    for ent in doc.ents:
        if ent.label_ in important_entities:
            entity = Entity(ent)
            if not contains_stem(entities, entity):
                entities.append(entity)

    for entity in entities:
        if entity.freq > 1:
            article_result.detected_mse.append(entity)
        else:
            article_result.detected_lse.append(entity)


def modified_frequency_analysis(doc, article_result):
    important_entities = ['PERSON', 'ORG', 'GPE', 'EVENT']
    entities = []

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


def frequency_analysis(doc, article_result):
    entities = []

    for ent in doc.ents:
        entity = Entity(ent)
        if not contains(entities, entity):
            entities.append(entity)

    for entity in entities:
        if entity.freq > 1:
            article_result.detected_mse.append(entity)
        else:
            article_result.detected_lse.append(entity)


def main():
    nlp = spacy.load("en_core_web_lg")
    directory = "/home/harsh/Downloads/data/ner-eval-collection-master/plainTextFiles/"
    results = []

    for i in range(0, 2):
        filename = directory + str(i) + ".txt"
        file = open(filename, "r")
        file_content = file.read()
        file_content = file_content.split("<delim>")
        article_text = file_content[0]
        doc = nlp(article_text)

        if file_content[1]:
            file_content[1].strip()
            mse_text = file_content[1].replace("[", "").replace("]", "").replace("\n", "")
            mse_text = mse_text.split(",")

        if file_content[2]:
            file_content[2].strip()
            lse_text = file_content[2].replace("[", "").replace("]", "").replace("\n", "")
            lse_text = lse_text.split(",")

        article_result = Result(i, article_text, mse_text, lse_text)
        stemmed_frequency_analysis(doc, article_result)
        results.append(article_result)
        print(article_result.toString())
        # graph = Graphs(results)
        # graph.graph2()


if __name__ == "__main__":
    main()
