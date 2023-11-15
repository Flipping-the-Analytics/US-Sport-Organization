from performance import Performance

# class for storing (and eventually analyzing) the performances of a gymnast
class Gymnast:
    def __init__(self, name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        self.name = name
        self.performances = [Performance(gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)]

    def addperformance(self, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        self.performances.append(Performance(gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score))

    def displayperformances(self):
        for i in range(len(self.performances)):
            print("name: " + self.name, end = " | ")
            self.performances[i].displayperformance()