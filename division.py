from gymnast import Gymnast

# class for storing (and eventually analyzing) each gymnast in either the men's or women's division
class Division:
    def __init__(self, gender):
        self.gender = gender
        self.gymnasts = {}
    
    def addperformance(self, name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        if name in self.gymnasts:
            self.gymnasts[name].addperformance(name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)
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
      
    def numberofpeoplebetweengymnastandfirstplace(self, apparatus, name):
        gymnast_score = None
        firstplace_score = self.findingmax(apparatus)
        count = 0
        apparatus_performances = []
        unique_gymnast_names = set()
        apparatus_names = []
        # Find the score of the specified gymnast
        for i in self.gymnasts.values():
            if i.name == name:
                gymnast_score = i.findingmax(apparatus)
                break
        # Iterate through all gymnasts and their performances and append to list
        for i in self.gymnasts.values():
            for j in i.performances:
                if j.apparatus == apparatus:
                    if i.name not in unique_gymnast_names:
                        cl += 1
                        apparatus_performances.append(j)
                        unique_gymnast_names.add(i.name)
        for performance in apparatus_performances:
             apparatus_names.append(performance.name)
        #print(apparatus_names)
        # Count the number of unique gymnasts between the specified gymnast and the first place
        for i in apparatus_names:
            if i == name:
                break
            count += 1
        score_difference = firstplace_score - gymnast_score
        print('gymnast score:', gymnast_score)
        print('people between:', count)
        print('score difference:', score_difference)
        print(count * score_difference)


    # def test(self):
    #     print('hi')
        
    #     self.gymnasts['Simone BILES'].numberofpeoplebetweengymnastandfirstplace('UB')

    


    
