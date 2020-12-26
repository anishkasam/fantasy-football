import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# read and import all the csv files
corr2017 = pd.read_csv("correlations/2017correlations.csv")
corr2018 = pd.read_csv("correlations/2018correlations.csv")
corr2019 = pd.read_csv("correlations/2019correlations.csv")

# x coordinates for dashed line at y = 0
flatline = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
flatlinex = np.array(flatline)

# open the 2017 correlations file
with open("correlations/2017correlations.csv", "r") as f:
  reader = csv.reader(f)

  # loop through every player in the file
  for i in range(len(corr2017)):
    correlation = corr2017["Correlation"][i]
    gamesplayed = corr2017["Games Played"][i]

    # lists to store x and y data for graphs
    xdata = []
    ydata = []

    # if the relationship is strong, the player has played more than half the season, and the player is a top 200 player
    if abs(correlation) > 0.6 and gamesplayed > 8 and i < 200:
      playername = corr2017["Player Name"][i]

      # iterate through every game (16 max) to copy player stats
      for k in range(1, 16):
        pointcolumn = "G" + str(k) + "P"
        oppteamcolumn = "G" + str(k) + "DR"
        
        # check if stats are valid numbers
        if abs(corr2017[pointcolumn][i]) > 0.01:
          ydata.append(corr2017[pointcolumn][i])
          xdata.append(corr2017[oppteamcolumn][i])

      # create scatter plot and set axis titles  
      plt.scatter(xdata, ydata)
      plt.title("Effect of Defense Strength on " + str(playername) + " in 2017")
      plt.xlabel("Defense Ranking (1-32) | Correlation = " + str(correlation))
      plt.ylabel("Fantasy Production Above/Below Yearly Mean")

      # create LSRL and y = 0 line
      x = np.array(xdata)
      y = np.array(ydata)
      m, b = np.polyfit(x, y, 1)
      plt.plot(x, m*x + b)
      plt.plot(flatlinex, 0*flatlinex, linestyle = "--", dashes = (5, 5), color = "black")

      plt.show()

# repeat same process above for 2018 correlations
with open("correlations/2018correlations.csv", "r") as f:
  reader = csv.reader(f)

  for i in range(len(corr2018)):
    correlation = corr2018["Correlation"][i]
    gamesplayed = corr2018["Games Played"][i]

    xdata = []
    ydata = []

    if abs(correlation) > 0.6 and gamesplayed > 8 and i < 200:
      playername = corr2018["Player Name"][i]

      for k in range(1, 16):
        pointcolumn = "G" + str(k) + "P"
        oppteamcolumn = "G" + str(k) + "DR"
        
        if abs(corr2018[pointcolumn][i]) > 0.01:
          ydata.append(corr2018[pointcolumn][i])
          xdata.append(corr2018[oppteamcolumn][i])
        
      plt.scatter(xdata, ydata)
      plt.title("Effect of Defense Strength on " + str(playername) + " in 2018")
      plt.xlabel("Defense Ranking (1-32) | Correlation = " + str(correlation))
      plt.ylabel("Fantasy Production Above/Below Yearly Mean")

      x = np.array(xdata)
      y = np.array(ydata)
      m, b = np.polyfit(x, y, 1)
      plt.plot(x, m*x + b)
      plt.plot(flatlinex, 0*flatlinex, linestyle = "--", dashes = (5, 5), color = "black")

      plt.show()

# repeat same process above for 2019 correlations
with open("correlations/2019correlations.csv", "r") as f:
  reader = csv.reader(f)

  for i in range(len(corr2019)):
    correlation = corr2019["Correlation"][i]
    gamesplayed = corr2019["Games Played"][i]

    xdata = []
    ydata = []

    if abs(correlation) > 0.6 and gamesplayed > 8 and i < 200:
      playername = corr2019["Player Name"][i]

      for k in range(1, 16):
        pointcolumn = "G" + str(k) + "P"
        oppteamcolumn = "G" + str(k) + "DR"
        
        if abs(corr2019[pointcolumn][i]) > 0.01:
          ydata.append(corr2019[pointcolumn][i])
          xdata.append(corr2019[oppteamcolumn][i])
        
      plt.scatter(xdata, ydata)
      plt.title("Effect of Defense Strength on " + str(playername) + " in 2019")
      plt.xlabel("Defense Ranking (1-32) | Correlation = " + str(correlation))
      plt.ylabel("Fantasy Production Above/Below Yearly Mean")

      x = np.array(xdata)
      y = np.array(ydata)
      m, b = np.polyfit(x, y, 1)
      plt.plot(x, m*x + b)
      plt.plot(flatlinex, 0*flatlinex, linestyle = "--", dashes = (5, 5), color = "black")

      plt.show()