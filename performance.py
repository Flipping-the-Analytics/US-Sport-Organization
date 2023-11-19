# storage class for the values associated with a gymnast's performance
class Performance:
    def __init__(self, gender, country, date, competition, round, location, apparatus, rank, dscore, escore, penalty, score):
        self.gender = gender
        self.country = country
        self.date = date
        self.competition = competition
        self.round = round
        self.location = location
        self.apparatus = apparatus
        self.rank = int(rank) if len(rank) > 0 else -1
        self.dscore = float(dscore)
        self.escore = float(escore)
        self.penalty = penalty if len(penalty) > 0 else 0
        self.score = float(score)

    def displayperformance(self):
        print("gender: " + self.gender, end = " | ")
        print("country: " + self.country, end = " | ")
        print("date: " + self.date, end = " | ")
        print("competition: " + self.competition, end = " | ")
        print("round: " + self.round, end = " | ")
        print("location " + self.location, end = " | ")
        print("apparatus: " + self.apparatus, end = " | ")
        print("rank: " + str(self.rank), end = " | ")
        print("dscore: " + str(self.dscore), end = " | ")
        print("escore: " + str(self.escore), end = " | ")
        print("penalty: " + str(self.penalty), end = " | ")
        print("score: " + str(self.score))