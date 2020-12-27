# cleans weekly data from online (https://www.fantasyfootballdatapros.com/csv_files)

import pandas as pd
import csv

files = ["2017/week1.csv", "2017/week2.csv", "2017/week3.csv", "2017/week4.csv", "2017/week5.csv", "2017/week6.csv", "2017/week7.csv", "2017/week8.csv", "2017/week9.csv", "2017/week10.csv", "2017/week11.csv", "2017/week12.csv", "2017/week13.csv", "2017/week14.csv", "2017/week15.csv", "2017/week16.csv", "2017/week17.csv"]

for file in files:
  stats = pd.read_csv(file)

  # format: [player name, games played, total fantasy points, average fantasy points]
  playerprofiles = []

  with open(file, "r") as f:
    reader = csv.reader(f)

    playercount = len(list(reader)) - 2
    for i in range(playercount):
      playername = stats["Player"][i]
      position = stats["Pos"][i]

      if position == "FB" or position == "HB":
        position = "RB"

      team = stats["Tm"][i]

      fantasypoints = 0
      # negative stats
      fantasypoints -= (stats["FL"][i] * 2)
      fantasypoints -= (stats["Int"][i] * 2)
      # positive stats
      fantasypoints += (stats["PassingYds"][i] * 0.04)
      fantasypoints += (stats["PassingTD"][i] * 4)
      fantasypoints += (stats["RushingYds"][i] * 0.1)
      fantasypoints += (stats["RushingTD"][i] * 6)
      fantasypoints += (stats["ReceivingYds"][i] * 0.1)
      fantasypoints += (stats["ReceivingTD"][i] * 6)
      fantasypoints += (stats["Rec"][i])

      profile = [playername, position, team, round(fantasypoints, 2)]
      playerprofiles.append(profile)

  with open(file, "w") as file:
    writer = csv.writer(file)

    headers = ["Player Name", "Position", "Team", "Total Fantasy Points"]
    writer.writerow(headers)
    writer.writerows(playerprofiles)

