# cleans ranking data from online (https://www.fantasypros.com/nfl/points-allowed.php?year=2018)

import pandas as pd
import csv

file = "2019rankings.csv"

rankings = pd.read_csv(file)

teamprofiles = []

with open(file, "r") as f: 
  reader = csv.reader(f)

  teams = len(list(reader)) - 2
  for i in range(teams):
    teamname = rankings["Team"][i]

    if teamname == "Arizona Cardinals":
      teamname = "ARI"
    elif teamname == "anta Falcons":
      teamname = "ATL"
    elif teamname == "Baltimore Ravens":
      teamname = "BAL"
    elif teamname == "Buffalo Bills":
      teamname = "BUF"
    elif teamname == "Carolina Panthers":
      teamname = "CAR"
    elif teamname == "Chicago Bears":
      teamname = "CHI"
    elif teamname == "Cincinnati Bengals":
      teamname = "CIN"
    elif teamname == "Cleveland Browns":
      teamname = "CLE"
    elif teamname == "Dallas Cowboys":
      teamname = "DAL"
    elif teamname == "Denver Broncos":
      teamname = "DEN"
    elif teamname == "Detroit Lions":
      teamname = "DET"
    elif teamname == "Green Bay Packers":
      teamname = "GNB"
    elif teamname == "Houston Texans":
      teamname = "HOU"
    elif teamname == "Indianapolis Colts":
      teamname = "IND"
    elif teamname == "Jacksonville Jaguars":
      teamname = "JAX"
    elif teamname == "Kansas City Chiefs":
      teamname = "KAN"
    elif teamname == "Las Vegas Raiders":
      teamname = "OAK"
    elif teamname == "Los Angeles Chargers":
      teamname = "LAC"
    elif teamname == "Los Angeles Rams":
      teamname = "LAR"
    elif teamname == "Miami Dolphins":
      teamname = "MIA"
    elif teamname == "Minnesota Vikings":
      teamname = "MIN"
    elif teamname == "New England Patriots":
      teamname = "NWE"
    elif teamname == "New Orleans Saints":
      teamname = "NOR"
    elif teamname == "New York Giants":
      teamname = "NYG"
    elif teamname == "New York Jets":
      teamname = "NYJ"
    elif teamname == "Philadelphia Eagles":
      teamname = "PHI"
    elif teamname == "Pittsburgh Steelers":
      teamname = "PIT"
    elif teamname == "San Francisco 49ers":
      teamname = "SFO"
    elif teamname == "Seattle Seahawks":
      teamname = "SEA"
    elif teamname == "Tampa Bay Buccaneers":
      teamname = "TAM"
    elif teamname == "Tennessee Titans":
      teamname = "TEN"
    elif teamname == "Washington Football Team":
      teamname = "WAS"

    qbrank = 33 - rankings["QBRank"][i]
    rbrank = 33 - rankings["RBRank"][i]
    wrrank = 33 - rankings["WRRank"][i]
    terank = 33 - rankings["TERank"][i]

    teamprofile = [teamname, qbrank, rbrank, wrrank, terank]
    teamprofiles.append(teamprofile)

with open(file, "w") as f:
  writer = csv.writer(f)

  headers = ["Team", "QB Rank", "RB Rank", "WR Rank", "TE Rank"]
  writer.writerow(headers)
  writer.writerows(teamprofiles)