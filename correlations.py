import pandas as pd
import csv
from yearlydata import *

yearlystats = pd.read_csv("yearlydata/2019.csv")
weeks = ["weeklydata/2019/week1.csv", "weeklydata/2019/week2.csv", "weeklydata/2019/week3.csv", "weeklydata/2019/week4.csv", "weeklydata/2019/week5.csv", "weeklydata/2019/week6.csv", "weeklydata/2019/week7.csv", "weeklydata/2019/week8.csv", "weeklydata/2019/week9.csv", "weeklydata/2019/week10.csv", "weeklydata/2019/week11.csv", "weeklydata/2019/week12.csv", "weeklydata/2019/week13.csv", "weeklydata/2019/week14.csv", "weeklydata/2019/week15.csv", "weeklydata/2019/week16.csv", "weeklydata/2019/week17.csv"]

playerprofiles = []

for i in range(len(yearlystats)): 
  playername = yearlystats["Player Name"][i]
  yearlyaverage = yearlystats["Average Fantasy Points"][i]

  profile = [playername]

  xdata = []
  ydata = []

  for file in range(len(weeks)):
    with open(weeks[file], "r") as f:
      reader = csv.reader(f)
      weeklystats = pd.read_csv(f)

      for k in range(len(weeklystats)):
        if playername == weeklystats["Player Name"][k]:
          points = yearlyaverage - (weeklystats["Total Fantasy Points"][k])
          oppteam = weeklystats["Opposing Team Rank"][k]

          xdata.append(oppteam)
          ydata.append(points)

          profile.append(round(points, 2))
          profile.append(oppteam)
  
  x = pd.Series(xdata)
  y = pd.Series(ydata)
  correlation = x.corr(y)

  profile.insert(1, round(correlation, 2))
  playerprofiles.append(profile)

  with open("correlations/2019correlations.csv", "w") as f:
    writer = csv.writer(f)

    headers = ["Player Name", "Correlation", "G1P", "G1DR", "G2P", "G2DR", "G3P", "G3DR", "G4P", "G4DR", "G5P", "G5DR", "G6P", "G6DR", "G7P", "G7DR", "G8P", "G8DR", "G9P", "G9DR", "G10P", "G10DR", "G11P", "G11DR", "G12P", "G12DR", "G13P", "G13DR", "G14P", "G14DR", "G15P", "G15DR", "G16P", "G16DR"]
    writer.writerow(headers)
    writer.writerows(playerprofiles)