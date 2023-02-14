# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

y = 42000


names = ['1992', '1993', '1994', '1995']
vals = [df.loc[1992], df.loc[1993], df.loc[1994], df.loc[1995]]
means = np.mean(vals, axis=1)
errors = 1.96*np.std(vals, axis=1) / np.sqrt(len(df.T))

colours = [(1,1,1), (1,1,1), (1,1,1), (1,1,1)]
for i in range(4):
    if means[i] + errors[i] < y:
        colours[i] = (0,0,1)
    elif means[i] - errors[i] > y:
        colours[i] = (1,0,0)

fig, ax = plt.subplots()
sns.barplot(data=df.T, palette=colours, estimator=np.mean, ci=95)
ax.plot([-0.5, 3.5], [y, y], 'k')

ax.set_xticks(np.arange(4))
ax.set_xticklabels(names)
ax.set_ylabel('Random Data')
ax.set_xlabel('year')
ax.set_title(f'A plot of the mean values for each year, with error bars indicating a 95% confidence interval. \n The horizontal bar shows the chosen value of y={y}. \n Years whose confidence interval contains y are shown in white, \n while those above and below y are shown in red and blue respectively.')


plt.show()