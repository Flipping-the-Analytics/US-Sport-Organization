from division import Division

# class for generating a potential olympic team for men and women
class TeamGenerator:
    def __init__(self):
        self.wdivision = Division("w", 1.4)
        self.mdivision = Division("m", 0.8)

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

    def generateteams(self):
        print("Women's Division")
        self.wdivision.maketeam(["BB", "UB", "FX", "VT"])
        print("Men's Division")
        self.mdivision.maketeam(["FX", "HB", "PB", "PH", "SR", "VT"])

    # use for testing internal functions
    def test(self):
        self.wdivision.maketeam(["BB", "UB", "FX", "VT"])
        return
        