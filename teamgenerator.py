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

    # use for testing internal functions
    def test(self):
        return
        
