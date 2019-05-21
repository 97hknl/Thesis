class Result:

    def __init__(self, index, article_text, most_salient_entities, less_salient_entities):
        self.index = index
        self.article_text = article_text
        self.most_salient_entities = most_salient_entities
        self.less_salient_entities = less_salient_entities
        self.detected_most_salient_entities = []
        self.detected_less_salient_entities = []

    def percentageExtraMostSalientEntities(self):
        result = 0
        for item in self.detected_most_salient_entities:
            for item2 in self.most_salient_entities:
                if item.text != item2:
                    result += 1
        return result/len(self.most_salient_entities)

    def percentageExtraLessSalientEntities(self):
        result = 0
        for item in self.detected_less_salient_entities:
            for item2 in self.less_salient_entities:
                if item.text != item2:
                    result += 1
        return result/len(self.less_salient_entities)

    def percentageLessMostSalientEntities(self):
        result = 0
        for item in self.most_salient_entities:
            for item2 in self.detected_most_salient_entities:
                if item != item2.text:
                    result += 1
        return result/len(self.most_salient_entities)

    def percentageLessLessSalientEntities(self):
        result = 0
        for item in self.less_salient_entities:
            for item2 in self.detected_less_salient_entities:
                if item != item2.text:
                    result += 1
        return result/len(self.less_salient_entities)
