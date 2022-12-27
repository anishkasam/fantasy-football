import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

yearlydata = pd.read_csv("2020data/2020yearly.csv")
defenses = pd.read_csv("2020data/2020defenses.csv")
schedules = pd.read_csv("2020data/2020schedule.csv")

yearlydata = yearlydata[yearlydata.get("Pos").isin(["QB", "RB", "WR", "TE"])]
yearlydata = yearlydata[yearlydata.get("G") >= 2]
yearlydata = yearlydata.drop(["Age", "GS", "Tgt", "Int", "Fumbles", "FumblesLost", "ReceivingYds", "ReceivingTD", "RushingYds", "RushingTD", "PassingYds", "PassingTD", "PassingAtt", "RushingAtt", "Rec"], axis = 1)
yearlydata["AvgFantasyPoints"] = yearlydata.get("FantasyPoints") / yearlydata.get("G")
yearlydata = yearlydata.rename(columns = {"Tm": "Team"})
yearlydata = yearlydata.sort_values(by = "Player")
yearlydata = yearlydata.set_index("Player")

for i in range(1, 17):
  weeklydata = pd.read_csv("2020data/2020weekly/week" + str(i) + ".csv")
  weeklydata = weeklydata[weeklydata.get("Pos").isin(["QB", "RB", "WR", "TE"])]
  weeklydata = weeklydata.rename(columns = {"PPRFantasyPoints": "Week " + str(i)})
  weeklydata = weeklydata.drop(["StandardFantasyPoints", "HalfPPRFantasyPoints", "ReceivingYds", "ReceivingTD", "RushingYds", "RushingTD", "PassingYds", "PassingTD", "PassingAtt", "RushingAtt", "Rec", "Int", "Cmp", "Tgt", "FL", "Tm", "Pos"], axis = 1)
  weeklydata = weeklydata.sort_values(by = "Player")
  weeklydata = weeklydata.set_index("Player")

  if i == 1:
    data = pd.merge(yearlydata, weeklydata, left_index = True, right_index = True)
  else:
    data = data.merge(weeklydata, left_index = True, right_index = True, how = "left")

schedules = schedules.drop(["W17", "W18"], axis = 1)

def removeAway(x):
  x = x.replace("@", "")
  x = x.replace("GB", "GNB")
  x = x.replace("NO", "NOR")
  x = x.replace("LV", "LVR")
  x = x.replace("TB", "TAM")
  x = x.replace("KC", "KAN")
  x = x.replace("SF", "SFO")
  x = x.replace("NE", "NWE")
  return x

def correlation(player):
  try:
    pointdiffs = []
    rankings = []
    team = data.loc[player].get("Team")
    pos = data.loc[player].get("Pos")

    for i in range(1, 17):
      points = data.loc[player].get("Week " + str(i))
      opponent = schedules.loc[team].get("W" + str(i))

      if (opponent == "BYE" or points == "NaN"):
        continue

      pointdiff = points - data.loc[player].get("AvgFantasyPoints")
      ranking = defenses.loc[opponent].get(pos + " Rank")

      pointdiffs.append(round(pointdiff, 2))
      rankings.append(ranking)
    
    x = pd.Series(rankings)
    y = pd.Series(pointdiffs)

    return round(x.corr(y), 2)
  except:
    return 0
def graph(player):
  pointdiffs = []
  rankings = []
  team = data.loc[player].get("Team")
  pos = data.loc[player].get("Pos")

  for i in range(1, 17):
    points = data.loc[player].get("Week " + str(i))
    opponent = schedules.loc[team].get("W" + str(i))

    if (opponent == "BYE" or points == "NaN"):
      continue

    pointdiff = points - data.loc[player].get("AvgFantasyPoints")
    ranking = defenses.loc[opponent].get(pos + " Rank")

    pointdiffs.append(round(pointdiff, 2))
    rankings.append(ranking)
  
  x = pd.Series(rankings)
  y = pd.Series(pointdiffs)

  plt.scatter(x, y)
  plt.title("Effect of Defense Strength on " + str(player) + " in 2017")
  plt.xlabel("Defense Ranking (1-32) | Correlation = " + str(correlation(player)))
  plt.ylabel("Fantasy Production Above/Below Yearly Mean")
  xdata = np.array(x)
  ydata = np.array(y)
  m, b = np.polyfit(xdata, ydata, 1)
  plt.plot(x, m*x + b)
  plt.show()

schedules["Team"] = schedules["Team"].apply(removeAway)
schedules = schedules.set_index("Team")
for i in range(1,17):
  schedules["W" + str(i)] = schedules["W" + str(i)].apply(removeAway)

defenses = defenses.set_index("Team")

data = data.assign(Correlation = data.index.map(correlation))
data = data.assign(AbsCorrelation = data.get("Correlation").apply(abs))
sigdata = data[data.get("AvgFantasyPoints") > 6].sort_values("AbsCorrelation", ascending = False)
sigdata = sigdata[sigdata.get("AbsCorrelation") > 0.6]
sigdata = sigdata[sigdata.get("G") > 6]

print(data)
print(sigdata)