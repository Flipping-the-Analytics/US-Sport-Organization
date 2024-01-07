import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt 
from pandas.plotting import table 
from gymnast import Gymnast

# class for storing (and eventually analyzing) each gymnast in either the men's or women's division
class Division:
    def __init__(self, gender, srange, apparatuses):
        self.gender = gender
        self.gymnasts = {}
        self.srange = srange
        apparatuses.sort()
        self.apparatuses = apparatuses 
        self.total = 30000
        self.team = None
        self.events = None
        self.sfdata = None
    
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
            couldplace, score = self.gymnasts[gymnast].medalopportunity(apparatus, maxscore, self.srange)
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

        for performance in apparatus_performances:
            if gymnast_score <= performance.score < firstplace_score:
                count += 1
                
        
        score_difference = firstplace_score - gymnast_score
        # print('gymnast score:', gymnast_score)
        # print('people between:', count)
        # print('score difference:', score_difference)
        # print(round(count * score_difference,5))
        return round(count*score_difference,5)
    

    def amountoff(self):

        j=0
        data={}
        peoplewithchance=set([])
        for app in self.apparatuses:
            medalsortedList=self.medalopportunity(app,self.findingmax(app))
            for people in medalsortedList:
                peoplewithchance.add(people[0])

        while(j<len(self.apparatuses)): 
            for people in peoplewithchance:
                if(people in data):
                    data[people].append(tuple([self.apparatuses[j],self.numberofpeoplebetweengymnastandfirstplace(self.apparatuses[j],people)]))
                else:    
                    data[people]=[tuple([self.apparatuses[j],self.numberofpeoplebetweengymnastandfirstplace(self.apparatuses[j],people)])]
            j=j+1
        # print(data)


        self.sfdata = data
    
    def determinesf(self, team):

        allaroundsf = {}
        for gymnast in team:
            allsf = 0
            for sf in self.sfdata[gymnast]:
                allsf += sf[1]
            allaroundsf[gymnast] = allsf
        allaround1 = min(allaroundsf, key=lambda x: allaroundsf[x])
        allaroundsf.pop(allaround1)
        allaround2 = min(allaroundsf, key=lambda x: allaroundsf[x])

        apparatustotals = {}
        appparticipants = {"AA": [allaround1, allaround2]}
        for apparatus in self.apparatuses:
            gymnastvalues = {}
            for gymnast in team:
                scorefactor = [val[1] for val in self.sfdata[gymnast] if val[0] == apparatus][0]
                gymnastvalues[gymnast] = scorefactor
            
            apparatustotals[apparatus] = 0
            apparatustotals[apparatus] += gymnastvalues[allaround1]
            apparatustotals[apparatus] += gymnastvalues[allaround2]
            gymnastvalues.pop(allaround1)
            gymnastvalues.pop(allaround2)

            appparticipants[apparatus] = [allaround1]
            appparticipants[apparatus].append(allaround2)
            thirdparticipant = min(gymnastvalues, key=lambda x: gymnastvalues[x])
            apparatustotals[apparatus] += gymnastvalues[thirdparticipant]
            appparticipants[apparatus].append(thirdparticipant)
            gymnastvalues.pop(thirdparticipant)
            fourthparticipant = min(gymnastvalues, key=lambda x: gymnastvalues[x])
            # apparatustotals[apparatus] += gymnastvalues[fourthparticipant]
            appparticipants[apparatus].append(fourthparticipant)
            gymnastvalues.pop(fourthparticipant)

            gymnastvalues.clear()

        sftotal = sum(apparatustotals.values())
        return sftotal, team, appparticipants

    def maketeam(self):

        self.amountoff()

        possibleteams = []
        team = set([])
        gymnasts = [gymnast for gymnast in self.sfdata]
        numgym = len(gymnasts)
        for i in range(numgym):
            if i + 4 < numgym:
                team.add(gymnasts[i])
                for j in range(i + 1, numgym):
                    if j + 3 < numgym:
                        team.add(gymnasts[j])
                        for k  in range(j + 1, numgym):
                            if k + 2 < numgym:
                                team.add(gymnasts[k])
                                for l in range(k + 1, numgym):
                                    if l + 1 < numgym:
                                        team.add(gymnasts[l])
                                        for m in range(l + 1, numgym):
                                            team.add(gymnasts[m])
                                            possibleteams.append(tuple(team))
                                            team.remove(gymnasts[m])
                                        team.remove(gymnasts[l])
                                team.remove(gymnasts[k])
                        team.remove(gymnasts[j])
                team.remove(gymnasts[i])

        for tm in possibleteams:
            temptotal, tempteam, tempevents = self.determinesf(tm)
            if temptotal < self.total:
                self.total = temptotal
                self.team = sorted(tempteam)
                self.events = tempevents
        
        print("Team")
        for gymnast in self.team:
            if self.team.index(gymnast) != 4:
                print(gymnast, end = ", ")
            else:
                print(gymnast)
        print("Event Lineup")
        for event in self.events:
            print(event + ":", end = " ")
            for gymnast in self.events[event]:
                if self.events[event].index(gymnast) != 3 and (event != "AA" or self.events[event].index(gymnast) != 1):
                    print(gymnast, end = ", ")
                else:
                    print(gymnast)
        print("Score Factor Total: " + str(self.total))

    def displaytable(self):
        tabledata = []
        for gymnast in self.team:
            tabledata.append([])
            self.sfdata[gymnast] = sorted(self.sfdata[gymnast], key=lambda x: x[0])
            for datapair in self.sfdata[gymnast]:
                tabledata[-1].append(datapair[1])
            tabledata[-1].append(gymnast)
        iris = load_iris() 
         
        iris_df = pd.DataFrame(data=tabledata,
                               columns=self.apparatuses+["Gymnast Name"]) 
        
        grouped_dataframe = iris_df.groupby("Gymnast Name").mean().round(2) 
        grouped_dataframe["Gymnast Name"] = self.team 
        
        plt.figure(figsize=(12, 4))
        plt.title("Score factors in each apparatus")
        plt.axis('off')
        plt.subplots_adjust(top=0.8)

        table(ax=plt.gca(), data=grouped_dataframe.drop(['Gymnast Name'], axis=1), loc='center')

        plt.show()
            


    
