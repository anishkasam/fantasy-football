import pandas as pd
import csv

# read and import all csv files using pandas
yearlystats = pd.read_csv("yearlydata/2017.csv")
weeks = ["weeklydata/2017/week1.csv", "weeklydata/2017/week2.csv", "weeklydata/2017/week3.csv", "weeklydata/2017/week4.csv", "weeklydata/2017/week5.csv", "weeklydata/2017/week6.csv", "weeklydata/2017/week7.csv", "weeklydata/2017/week8.csv", "weeklydata/2017/week9.csv", "weeklydata/2017/week10.csv", "weeklydata/2017/week11.csv", "weeklydata/2017/week12.csv", "weeklydata/2017/week13.csv", "weeklydata/2017/week14.csv", "weeklydata/2017/week15.csv", "weeklydata/2017/week16.csv", "weeklydata/2017/week17.csv"]

playerprofiles = []

# iterate through every player that scored that year
for i in range(len(yearlystats)): 
  # pull player name and yearly average from that file
  playername = yearlystats["Player Name"][i]
  gamesplayed = yearlystats["Games Played"][i]
  yearlyaverage = yearlystats["Average Fantasy Points"][i]

  profile = [playername]

  xdata = []
  ydata = []

  # iterate through every weekly data file to find weeks where the selected player scored points
  for file in range(len(weeks)):
    with open(weeks[file], "r") as f:
      reader = csv.reader(f)
      weeklystats = pd.read_csv(f)

      # calculate their +/- from their yearly average and pull the opposing team's rank
      for k in range(len(weeklystats)):
        if playername == weeklystats["Player Name"][k]:
          points = (weeklystats["Total Fantasy Points"][k]) - yearlyaverage
          oppteam = weeklystats["Opposing Team Rank"][k]

          xdata.append(oppteam)
          ydata.append(points)

          profile.append(round(points, 2))
          profile.append(oppteam)
  
  # find the correlation between opposing team rank and fantasy +/-
  x = pd.Series(xdata)
  y = pd.Series(ydata)
  correlation = x.corr(y)

  profile.insert(1, gamesplayed)
  profile.insert(2, round(correlation, 2))
  playerprofiles.append(profile)

  # create new file with the correlation coefficient and the data from all the games they played (game number does not mean week number)
  with open("correlations/2017correlations.csv", "w") as f:
    writer = csv.writer(f)

    headers = ["Player Name", "Games Played", "Correlation", "G1P", "G1DR", "G2P", "G2DR", "G3P", "G3DR", "G4P", "G4DR", "G5P", "G5DR", "G6P", "G6DR", "G7P", "G7DR", "G8P", "G8DR", "G9P", "G9DR", "G10P", "G10DR", "G11P", "G11DR", "G12P", "G12DR", "G13P", "G13DR", "G14P", "G14DR", "G15P", "G15DR", "G16P", "G16DR", "G17P", "G17DR"]
    writer.writerow(headers)
    writer.writerows(playerprofiles)