

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the data set in data frame df
df = pd.read_csv("net_migration.csv")
print(df)

"""
creating multiple lines plot of data set with each data marked on line, 
setting limit to y-axis, giving title and labelling x and y axis in plot,
also setting their font sizes, adding legend and turning on the minor ticks 
on both axises of plot, and saving figure as png.
"""
#line plot with markers
plt.figure()
plt.plot(df.years, df["Australia"], marker='.')
plt.plot(df.years, df["Brazil"], marker='.')
plt.plot(df.years, df["Germany"], marker='.')
plt.plot(df.years, df["Spain"], marker='.')
plt.plot(df.years, df["Canada"], marker='.')
plt.ylim([-0.5e6, 1.0e6])
plt.title("Net Migration of Five Countries from 2000-2021", fontsize=13, y=1.03)
plt.xlabel("Years", fontsize=9)
plt.ylabel("net-migration (millions)", fontsize=9)
plt.legend(["AUS","BRA","GER","SPA","CAN"], fontsize=7)
plt.minorticks_on()
plt.savefig("Line_plot.png")
plt.show()

"""
creating multiple bar plot for five years from data set, setting limit to 
y-axis, giving title and labelling x and y axis in plot, also setting their 
font sizes, adding legend and turning rotation zero for xlabels in plot,
and saving figure as png.
"""
plt.figure()
plotdata = pd.DataFrame({
    "2016":[242184,82589,432017,89021,320494],
    "2017":[244875,56362,430803,167475,361274],
    "2018":[220307,67934,392587,339064,417974],
    "2019":[235860,69186,360560,458943,391914],
    "2020":[117929,56880,334055,208791,195181]},
    index=["AUS","BRA","GER","SPA","CAN"])
plotdata.plot(kind="bar")
plt.ylim([0e6, 1e6])
plt.title("Net Migration of Five Countries from 2016-2020", fontsize=13, y=1.03)
plt.xlabel("Countries", fontsize=9)
plt.ylabel("net-migration (millions)", fontsize=9)
plt.legend([2016,2017,2018,2019,2020], fontsize=7)
plt.xticks(rotation=0)
plt.savefig("Bar_plot.png")
plt.show()

"""
creating a pie plot for year 2021 from data set of five countries, 
also showing percentages and values using ptc argument, using explode to give 
space in each slice, giving title and adding legend to plot also setting their 
font sizes and positions, and saving figure as png.
"""
plt.figure()
countries = ["AUS","GER","BRA","SPA","CAN"]
net_migration_rate = np.array([117929,312735,20376,275022,195181])
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.0f}%\n({:d})".format(pct, absolute)
pie_explode = (0.01, 0.01, 0.01, 0.01, 0.01)
plt.pie(net_migration_rate, labels = countries,explode = pie_explode,
        autopct = lambda pct: func(pct, net_migration_rate))
plt.title("Net Migration of Five Countries in 2021", fontsize=13, y=1.01)
plt.legend(["AUS","BRA","GER","SPA","CAN"], fontsize=7, loc="upper right")
plt.savefig("Pie_plot.png")
plt.show()

