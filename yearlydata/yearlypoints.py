import pandas as pd
import csv

file = "2017.csv"

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
    gamesplayed = stats["G"][i]

    fantasypoints = 0
    # negative stats
    fantasypoints -= (stats["FumblesLost"][i] * 2)
    fantasypoints -= (stats["Int"][i] * 2)
    # positive stats
    fantasypoints += (stats["PassingYds"][i] * 0.04)
    fantasypoints += (stats["PassingTD"][i] * 4)
    fantasypoints += (stats["RushingYds"][i] * 0.1)
    fantasypoints += (stats["RushingTD"][i] * 6)
    fantasypoints += (stats["ReceivingYds"][i] * 0.1)
    fantasypoints += (stats["ReceivingTD"][i] * 6)
    fantasypoints += (stats["Rec"][i])

    averagepoints = fantasypoints / (stats["G"][i])

    profile = [playername, position, team, gamesplayed, round(fantasypoints, 2), round(averagepoints, 2)]
    playerprofiles.append(profile)

with open(file, "w") as file:
  writer = csv.writer(file)

  headers = ["Player Name", "Position", "Team", "Games Played", "Total Fantasy Points", "Average Fantasy Points"]
  writer.writerow(headers)
  writer.writerows(playerprofiles)

