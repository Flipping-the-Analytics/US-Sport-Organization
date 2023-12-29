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
        #This was a test that i couldn't finish
        #print(self.wdivision.medalopportunity(apparatus,score))

    # use for testing internal functions
    def test(self):
        return
        
