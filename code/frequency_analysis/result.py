from nltk.stem import PorterStemmer

class Result:

    def __init__(self, index, article_text, mse, lse):
        self.index = index
        self.article_text = article_text
        self.mse = mse
        self.lse = lse
        self.detected_mse = []
        self.detected_lse = []
        self.stemmed_mse = self.stem(1)
        self.stemmed_lse = self.stem(2)

# use mode = 1 for most salient entities

    def toString(self):
        result = "Index : " + str(self.index) + "\n"
        result += "Article Text : " + self.article_text + "\n"

        result += "Most Salient Entities : " + "[" + ", ".join(str(x) for x in self.mse) + "]" + "\n"
        result += "Stemmed Most Salient Entities : " + repr(self.stemmed_mse) + "\n"
        result += "Detected Most Salient Entities : " + "[" + ", ".join(str(x.toString()) for x in self.detected_mse) + "]" + "\n"

        result += "Less Salient Entities : " + "[" + ", ".join(str(x) for x in self.lse) + "]" + "\n"
        result += "Stemmed Less Salient Entities : " + repr(self.stemmed_lse) + "\n"
        result += "Detected Less Salient Entities : " + "[" + ", ".join(str(x.toString()) for x in self.detected_lse) + "]" + "\n"
        result += "--------------------------------------------------------------"
        return result

    def stem(self, mode):
        porter = PorterStemmer()
        result = []

        if mode == 1:
            list = self.mse
        else:
            list = self.lse

        for item in list:
            item = item.split(" ")
            stemmed_entity = ""
            for word in item:
                stemmed_entity += porter.stem(word) + " "
            result.append(stemmed_entity.strip())

        return result

    def numTruePositives(self, mode):
        result = 0
        if mode == 1:
            for item in self.detected_mse:
                if item.text in self.mse:
                    result += 1
        else:
            for item in self.detected_lse:
                if item.text in self.lse:
                    result += 1

        return result

    def numFalsePositives(self, mode):
        result = 0
        if mode == 1:
            for item in self.detected_mse:
                if item.text not in self.mse:
                    result += 1
        else:
            for item in self.detected_lse:
                if item.text not in self.lse:
                    result += 1

        return result

    def numFalseNegatives(self, mode):
        result = 0
        if mode == 1:
            for item in self.mse:
                for item2 in self.detected_mse:
                    if item != item2.text:
                        result += 1
        else:
            for item in self.lse:
                for item2 in self.detected_lse:
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