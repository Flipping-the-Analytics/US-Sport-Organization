from performance import Performance

# class for storing (and eventually analyzing) the performances of a gymnast
class Gymnast:
    def __init__(self, name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        self.name = name
        self.performances = [Performance(name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)]

    def addperformance(self, name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        self.performances.append(Performance(name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score))

    def displayperformances(self):
        for i in range(len(self.performances)):
            print("name: " + self.name, end = " | ")
            self.performances[i].displayperformance()

    def findingmax(self, apparatus):
        scoresappartus=[x.score for x in self.performances if x.apparatus==apparatus ] + [0]
        return(round(max(scoresappartus),2))
    
    def medalopportunity(self, apparatus, maxscore, srange=1.4):
        couldplace = False
        score = maxscore - srange
        # returns true and score if a performance within the 
        if (self.performances[0].country != "USA"):
            return False, score
        for i in range(len(self.performances)):
            if self.performances[i].apparatus == apparatus and self.performances[i].score > score:
                couldplace = True
                score = self.performances[i].score
        return couldplace, score