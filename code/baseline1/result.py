class Result:

    def __init__(self, index, article_text, most_salient_entities, less_salient_entities):
        self.index = index
        self.article_text = article_text
        self.most_salient_entities = most_salient_entities
        self.less_salient_entities = less_salient_entities
        self.detected_most_salient_entities = []
        self.detected_less_salient_entities = []

    # sue mode = 1 for most salient entities
    def numTruePositives(self, mode):
        result = 0
        if mode == 1:
            for item in self.detected_most_salient_entities:
                if item.text in self.most_salient_entities:
                    result += 1
        else:
            for item in self.detected_less_salient_entities:
                if item.text in self.less_salient_entities:
                    result += 1

        return result

    def numFalsePositives(self, mode):
        result = 0
        if mode == 1:
            for item in self.detected_most_salient_entities:
                if item.text not in self.most_salient_entities:
                    result += 1
        else:
            for item in self.detected_less_salient_entities:
                if item.text not in self.less_salient_entities:
                    result += 1

        return result

    def numFalseNegatives(self, mode):
        result = 0
        if mode == 1:
            for item in self.most_salient_entities:
                for item2 in self.detected_most_salient_entities:
                    if item != item2.text:
                        result += 1
        else:
            for item in self.less_salient_entities:
                for item2 in self.detected_less_salient_entities:
                    if item != item2.text:
                        result += 1

        return result

    def precision(self, mode):
        TP = self.numTruePositives(mode)
        FP = self.numFalsePositives(mode)

        if TP + FP == 0:
            return -1
        else:
            return TP / (TP + FP)


    def recall(self, mode):
        TP = self.numTruePositives(mode)
        FN = self.numFalseNegatives(mode)

        if TP + FN == 0:
            return -1
        else:
            return TP / (TP + FN)

    def f1score(self, mode):
        pre = self.precision(mode)
        rec = self.recall(mode)

        if pre < 0 or rec < 0:
            return -1
        elif pre + rec == 0:
            return -2
        else:
            return 2 * (pre * rec) / (pre + rec)


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
