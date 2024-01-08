import csv
import matplotlib.pyplot as plt
import numpy as np
from teamgenerator import TeamGenerator

if __name__ == "__main__":
    teamgenerator = TeamGenerator()
    with open("US-Sport-Organization\data_2022_2023.csv", mode = "r", encoding='utf-8-sig', errors='replace') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            teamgenerator.addperformance(lines[1] + " " + lines[0], lines[2], lines[3], lines[4], lines[5], lines[6], 
                                         lines[7], lines[8], lines[9], lines[10], lines[11], lines[12], lines[13])
            
    # creating the dataset
    data = {'C':20, 'C++':15, 'Java':30, 'Python':35}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    plt.show()


    teamgenerator.generateteams()
