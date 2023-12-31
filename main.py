import csv
from teamgenerator import TeamGenerator

if __name__ == "__main__":
    teamgenerator = TeamGenerator()
    with open("US-Sport-Organization\data_2022_2023.csv", mode = "r", encoding='utf-8-sig', errors='replace') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            teamgenerator.addperformance(lines[1] + " " + lines[0], lines[2], lines[3], lines[4], lines[5], lines[6], 
                                         lines[7], lines[8], lines[9], lines[10], lines[11], lines[12], lines[13])
    # maleFX=teamgenerator.tester("m","FX")
    # maleVT=teamgenerator.tester("m","VT")
    # malePB=teamgenerator.tester("m","PB")
    # malePH=teamgenerator.tester("m","PH")
    # maleHB=teamgenerator.tester("m","HB")
    # maleSR=teamgenerator.tester("m","SR")

    # womenFX=teamgenerator.tester("w","FX")
    # womenVT=teamgenerator.tester("w","VT")
    # womenUB=teamgenerator.tester("w","UB")
    # womenBB=teamgenerator.tester("w","BB")
    # print(maleFX,maleVT,malePB,malePH,maleHB,maleSR,womenFX,womenVT,womenUB,womenBB)
    
    #womenFX=teamgenerator.tester("w","FX",womenFX)
    # teamgenerator.displayperformances()
    # teamgenerator.displayperformances()
    teamgenerator.test()
