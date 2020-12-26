import numpy 
import matplotlib.pyplot as plt
import pandas as pd
import csv

xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ydata = [10, 20, 30, 40, 50, 60, 70, 80, 90]

plt.scatter(xdata, ydata)
plt.title("Effect of Defense Strength on Player Production")
plt.xlabel("Defense Ranking (1-32)")
plt.ylabel("Fantasy Production Above/Below Yearly Mean")

x = pd.Series(xdata)
y = pd.Series(ydata)

# print(x.corr(y))