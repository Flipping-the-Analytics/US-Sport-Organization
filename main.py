import csv
from teamgenerator import TeamGenerator

if __name__ == "__main__":
    teamgenerator = TeamGenerator()
    with open("US-Sport-Organization\data_2022_2023.csv", mode = "r", errors='replace') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            teamgenerator.addperformance(lines[1] + " " + lines[0], lines[2], lines[3], lines[4], lines[5], lines[6], 
                                         lines[7], lines[8], lines[9], lines[10], lines[11], lines[12], lines[13])
    teamgenerator.displayperformances()