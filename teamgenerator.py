from division import Division

# class for generating a potential olympic team for men and women
class TeamGenerator:
    def __init__(self):
        self.wdivision = Division("w")
        self.mdivision = Division("m")

    def addperformance(self, name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        if gender == "w":
            self.wdivision.addperformance(name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)
        elif gender == "m":
            self.mdivision.addperformance(name, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score)

    def displayperformances(self):
        print("Women's Division:")
        self.wdivision.displayperformances()
        print("Men's Division:")
        self.mdivision.displayperformances()
    
    def tester(self,gender,apparatus,score=0):
        if(gender=="m"):
            return(self.mdivision.findingmax(apparatus))
        if(gender=="w"):  
            return(self.wdivision.findingmax(apparatus))
        # print(self.wdivision.medalopportunity("BB", self.wdivision.findingmax("BB")))

    # use for testing internal functions
    def test(self):
        self.wdivision.numberofpeoplebetweengymnastandfirstplace('FX', 'Madray JOHNSON')
        #self.wdivision.amountoff()
        # print ("BB", end="")
        # print(self.wdivision.medalopportunity("BB", self.wdivision.findingmax("BB")))
        # print ("UB", end="")
        # print(self.wdivision.medalopportunity("UB", self.wdivision.findingmax("UB")))
        # print ("FX", end="")
        # print(self.wdivision.medalopportunity("FX", self.wdivision.findingmax("FX")))
        # print ("VT", end="")
        # print(self.wdivision.medalopportunity("VT", self.wdivision.findingmax("VT")))
        # print ("VT-1", end="")
        # print(self.wdivision.medalopportunity("VT-1", self.wdivision.findingmax("VT-1")))
        # print ("VT-2", end="")
        # print(self.wdivision.medalopportunity("VT-2", self.wdivision.findingmax("VT-2")))
        return
        