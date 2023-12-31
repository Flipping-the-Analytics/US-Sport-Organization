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

        return float(max(scoresappartus))
    


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



        if(gymnast_score==None):
            return(3000)

        # Iterate through all gymnasts and their performances and append to list
        for i in self.gymnasts.values():
            perind = 0
            curind = 0
            bestscore = 0.0
            for j in i.performances:
                if j.apparatus == apparatus and j.score > bestscore:
                    bestscore = j.score
                    perind = curind
                curind += 1
            if i.performances[perind].apparatus == apparatus:
                apparatus_performances.append(i.performances[perind])
                unique_gymnast_names.add(i.name)




        apparatus_performances.sort(reverse=True)


        # #appends names to list
        # for performance in apparatus_performances:
        #      apparatus_names.append(performance.name)
        


        #print(apparatus_names)
        # Count the number of unique gymnasts between the specified gymnast and the first place
        
        # for i in apparatus_names:
        #     if i == name:
        #         break
        #     count += 1
        
          # Count the number of gymnasts between the specified gymnast and the first place
        for performance in apparatus_performances:
            if gymnast_score <= performance.score < firstplace_score:
                count += 1
                
        
        score_difference = firstplace_score - gymnast_score
        print('gymnast score:', gymnast_score)
        print('people between:', count)
        print('score difference:', score_difference)
        print(round(count * score_difference,5))
        return round(count*score_difference,5)

   


        #print(apparatus_names)
        # Count the number of unique gymnasts between the specified gymnast and the first place
        
        # for i in apparatus_names:
        #     if i == name:
        #         break
        #     count += 1
        
          # Count the number of gymnasts between the specified gymnast and the first place
        for performance in apparatus_performances:
            if gymnast_score <= performance.score < firstplace_score:
                count += 1
                
        
        score_difference = firstplace_score - gymnast_score
        print('gymnast score:', gymnast_score)
        print('people between:', count)
        print('score difference:', score_difference)
        print(count * score_difference)
        return count*score_difference

    


    

 def amountoff(self):

        j=0
        apparatus=["BB","UB","VT","FX",]
        data={}
        peoplewithchance=set([])
        for app in apparatus:
            medalsortedList=self.medalopportunity(app,self.findingmax(app))
            for people in medalsortedList:
                peoplewithchance.add(people[0])


        while(j<4):

            
            for people in peoplewithchance:
                if(people in data):
                    data[people].append(tuple([apparatus[j],self.numberofpeoplebetweengymnastandfirstplace(apparatus[j],people)]))
                else:    
                    data[people]=[tuple([apparatus[j],self.numberofpeoplebetweengymnastandfirstplace(apparatus[j],people)])]
                    
                    # data={medalsortedList[i][0]:(apparatus[j],self.numberofpeoplebetweengymnastandfirstplace(apparatus[j],medalsortedList[i][0]))}
            j=j+1
        print(data)

        return (data)