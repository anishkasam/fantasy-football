import pandas as pd
import csv

# read and import all csv files using pandas
rankings = pd.read_csv("rankings/2019rankings.csv")
schedule = pd.read_csv("schedules/2019schedule.csv")
yearlystats = pd.read_csv("yearlydata/2019.csv")
weeks = ["weeklydata/2019/week1.csv", "weeklydata/2019/week2.csv", "weeklydata/2019/week3.csv", "weeklydata/2019/week4.csv", "weeklydata/2019/week5.csv", "weeklydata/2019/week6.csv", "weeklydata/2019/week7.csv", "weeklydata/2019/week8.csv", "weeklydata/2019/week9.csv", "weeklydata/2019/week10.csv", "weeklydata/2019/week11.csv", "weeklydata/2019/week12.csv", "weeklydata/2019/week13.csv", "weeklydata/2019/week14.csv", "weeklydata/2019/week15.csv", "weeklydata/2019/week16.csv", "weeklydata/2019/week17.csv"]

# iterate through all the files in the weeks list (all the weekly data files)
for file in range(len(weeks)):
  playerprofiles = []

  with open(weeks[file], "r") as f:
    reader = csv.reader(f)
    weeklystats = pd.read_csv(f)

    # iterate through every line in each weekly data file
    for i in range(len(weeklystats)):
      # pull key data from each file from each line
      playername = weeklystats["Player Name"][i]
      position = weeklystats["Position"][i]
      team = weeklystats["Team"][i]
      points = weeklystats["Total Fantasy Points"][i]

      # pull the team that the player is playing against from the schedule file
      for k in range(len(schedule)):
        if team == schedule["Team"][k]:
          week = "W" + (str(file + 1))
          oppteam = schedule[week][k]

          # pull the ranking of the team the player is playing from the ranking file
          for j in range(len(rankings)):
            if oppteam == rankings["Team"][j]:
              if position == "QB":
                ranking = rankings["QB Rank"][j]
              elif position == "RB":
                ranking = rankings["RB Rank"][j]
              elif position == "WR":
                ranking = rankings["WR Rank"][j]
              elif position == "TE":
                ranking = rankings["TE Rank"][j]
              else:
                print("Invalid Position at line " + str((j+2)))

      # combine all of the above data into one list and append it to the master list
      profile = [playername, team, position, points, ranking]
      playerprofiles.append(profile)

  # rewrite that file with new, cleaned, and organized data
  with open(weeks[file], "w") as f:
    writer = csv.writer(f)

    headers = ["Player Name", "Position", "Team", "Total Fantasy Points", "Opposing Team Rank"]
    writer.writerow(headers)
    writer.writerows(playerprofiles)



