from gymnast import Gymnast

# class for storing (and eventually analyzing) each gymnast in either the men's or women's division
class Division:
    def __init__(self, gender):
        self.gender = gender
        self.gymnasts = {}
    
    def addperformance(self, name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        if name in self.gymnasts:
            self.gymnasts[name].addperformance(gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)
        else:
            self.gymnasts[name] = Gymnast(name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)
    
    def displayperformances(self):
        for gymnast in self.gymnasts:
            self.gymnasts[gymnast].displayperformances()

    def findingmax(self,apparatus):
        scoresappartus=[self.gymnasts[x].findingmax(apparatus) for x in self.gymnasts]
        scoresappartus.sort()
        return max(scoresappartus)
    
    def medalopportunity(self, apparatus, maxscore):

        # gets a list of all american gymnasts within a given range of the max score
        medalopportunity = []
        for gymnast in self.gymnasts:
            couldplace, score = self.gymnasts[gymnast].medalopportunity(apparatus, maxscore)
            if couldplace:
                medalopportunity.append(tuple([gymnast, score]))
        medalopportunitysorted = []

        # sorts gymnasts by their scores in descending order
        while(len(medalopportunity) > 0):
            index = 0
            for i in range(len(medalopportunity)):
                if medalopportunity[i][1] > medalopportunity[index][1]:
                    index = i
            temp = medalopportunity[index]
            medalopportunitysorted.append(temp)
            medalopportunity.pop(index)
        
        return(medalopportunitysorted)

    