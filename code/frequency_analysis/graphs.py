import matplotlib.pyplot as plt

class Graphs:

    def __init__(self, results):
        self.results = results

    def graph1(self):
        numMostSalientEntities = []
        numLessSalientEntities = []
        numDetectedMostSalientEntities = []
        numDetectedLessSalientEntities = []
        indices = []

        for result in self.results:
            numMostSalientEntities.append(len(result.most_salient_entities))
            numLessSalientEntities.append(len(result.less_salient_entities))
            numDetectedMostSalientEntities.append(len(result.detected_most_salient_entities))
            numDetectedLessSalientEntities.append(len(result.detected_less_salient_entities))
            indices.append(result.index)

        plt.plot(indices, numMostSalientEntities, label = "Number of Most Salient Entities")
        plt.plot(indices, numLessSalientEntities, label="Number of Less Salient Entities")
        plt.plot(indices, numDetectedMostSalientEntities, label="Number of Detected Most Salient Entities")
        plt.plot(indices, numDetectedLessSalientEntities, label="Number of Detected Less Salient Entities")

        plt.xlabel('Article index')
        plt.legend()
        plt.show()

    def graph2(self):
        indices = []
        f1scoresMostSalientEntities = []
        f1scoresLessSalientEntities = []

        for result in self.results:
            indices.append(result.index)
            f1scoresMostSalientEntities.append(result.f1score(1))
            f1scoresLessSalientEntities.append(result.f1score(2))

        plt.plot(indices, f1scoresMostSalientEntities, label = "F1 Scores for detecting most salient entities")
        plt.plot(indices, f1scoresMostSalientEntities, label = "F1 Scores for detecting less salient entities")

        plt.xlabel('Article index')
        plt.legend()
        plt.show()